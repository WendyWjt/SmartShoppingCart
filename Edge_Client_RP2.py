# Edge_Client_RP2.py
'''
    Checking out.
'''
from src.edge.TFLite_detection_image import get_item_dictionary
from src.edge.Edge_Client_Interface import Edge_Client_Interface

template = '{{ "device": "{}", "event": "{}", "content" : {} }}'

class Edge_Client_RP2(Edge_Client_Interface):
    def __init__(self):
        Edge_Client_Interface.__init__(self, "rpi2_000")


    def run(self):
        while True:
            try:
                # wait for "activate"
                message = self.getReplyFromFog()

                # send request
                request = template.format(self.id, "scan", {"item": get_item_dictionary()})
                self.sendRequestToFog(request)

                if request == "Quit":
                    if message != "Bye":
                        print("Edge Client: The Fog Server might not quit properly.")
                    break
            except Exception as e:
                print("Edge Client: Error occurs when talking to the Fog Server. Please restart the Edge Client.")
                print("Edge Client:", e)
                if request == "Quit":
                    break


if __name__ == "__main__":
    e = Edge_Client_RP2()
    e.run()