# Fog.py

import zmq
import sys
import time
import Global_Var


class Fog:
    def __init__(self):
        print("Fog Server starts. Fog Client starts.")
        self.context = zmq.Context()

        #####
        # Socket facing cloud
        self.frontend = self.context.socket(zmq.REQ)
        # self.frontend.setsockopt(zmq.SNDTIMEO, 2)   # Timeout: 2 sec
        # self.frontend.setsockopt(zmq.LINGER, 2)
        self.frontend.connect("tcp://" + Global_Var.CLOUD_IP + ":%s" % Global_Var.CLOUD_PORT)
        print("Fog: frontend (cloud) connect to port: tcp://" + Global_Var.CLOUD_IP + ":%s" % Global_Var.CLOUD_PORT)

        #####
        # Socket facing edge devices
        self.backend = self.context.socket(zmq.ROUTER)
        self.backend.bind("tcp://*:%s" % Global_Var.FOG_PORT)
        print("Fog: backend (edge) bind port: tcp://*:%s" % Global_Var.FOG_PORT)

        self.frames = {}
        self.frame_pair = {}

    def sendReplyToEdge(self, frame: str, reply: str):
        self.backend.send_multipart([frame.encode(), reply.encode()])
        print("Fog Server: Send reply to the Edge", frame, ":", reply)


    def sendRequestToCloud(self, request: str):
        self.frontend.send_string(request)
        print("Fog Server: Sending request to the Cloud:", request)


    def getRequestFromEdge(self) -> ("frame", "reply"):
        message = self.backend.recv_multipart()
        frame, message_edge = (message[0].decode("utf-8"), message[1].decode("utf-8"))
        print("Fog Server: Received request from Edge", frame, ":", message_edge)
        self.frames[frame] = True
        return frame, message_edge


    def getReplyFromCloud(self):
        message_cloud = self.frontend.recv().decode("utf-8")
        print ("Fog Server: Received reply from the Cloud:", message_cloud)
        return message_cloud

    ## TODO: not work properly now
    def disconnetAllFrame(self):
        for f in self.frames:
            if self.frames[f]:
                self.sendReplyToEdge(f, "Bye")


    def filter(self, frame, message_edge):
        try:  # tcl dbq # want to do filter here
            msg_dict = eval(message_edge)
        except Exception as e:
            self.sendReplyToEdge(frame, str({"status": 22, "content": {"msg": e}}))
        else:
            return msg_dict

    ## TODO: make it security & reliable
    def run(self):
        while True:
            try:
                # Receive message from the Edge first
                frame, message_edge = self.getRequestFromEdge()

                if message_edge == "Quit":
                    message_to_edge = "Bye"
                    self.sendReplyToEdge(frame, message_to_edge)
                    del self.frames[frame]
                    continue

                msg_dict = self.filter(frame, message_edge)
                if msg_dict == None:
                    continue

                if msg_dict["event"].lower() == "activate":
                    # send from rpi1, need to activate rpi2
                    frame2 = msg_dict["content"]["device"]
                    self.frame_pair[frame2] = frame
                    self.sendReplyToEdge(frame2, str({"event": "activate", "content": {"msg": "activate"}}))
                    continue


                # else, normal request
                # Pass the message to the Cloud
                request = message_edge
                self.sendRequestToCloud(request)

                #  Get the reply from the cloud.
                message_cloud = self.getReplyFromCloud()

                cloud_dict = eval(message_cloud)
                if cloud_dict["event"] == "scan":
                    self.sendReplyToEdge(self.frame_pair[frame], message_cloud)
                    continue

                self.sendReplyToEdge(frame, message_cloud)

                if message_cloud == "Bye":
                    print("Fog Server: The Cloud Server might not quit properly. Please restart server.")
                    self.disconnetAllFrame()
                    break
            except Exception as e:
                # for all frame connected, self.sendReplyToEdge(frame, "Bye")
                self.disconnetAllFrame()

                print("Fog Server: Error occurs when talking to the Cloud Server/Edge Client. Please restart the Fog Server.")
                print("Fog Server: ", e)
                break



    def __del__(self):
        print("Fog Server terminates. Fog Client terminates.")
        self.frontend.setsockopt(zmq.LINGER, 0)
        self.frontend.close()
        self.backend.setsockopt(zmq.LINGER, 0)
        self.backend.close()
        self.context.term()



if __name__ == "__main__":
    fog = Fog()
    fog.run()
