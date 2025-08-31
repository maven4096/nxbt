import time
import nxbt
from nxbt import Buttons

if __name__ == "__main__":

    # Init NXBT
    nx = nxbt.Nxbt()

    # Get a list of all available Bluetooth adapters
    adapters = nx.get_available_adapters()
    # Prepare a list to store the indexes of the
    # created controllers.
    controller_idxs = []
    # Loop over all Bluetooth adapters and create
    # Switch Pro Controllers
    for i in range(0, len(adapters)):
        index = nx.create_controller(
            nxbt.PRO_CONTROLLER,
            adapter_path=adapters[i],
            reconnect_address="78:20:A5:8B:3A:EE")
            #colour_body=[255,255,255],
            #colour_buttons=[255,255,255])
        controller_idxs.append(index)

    # Select the last controller for input
    controller_idx = controller_idxs[-1]

    nx.wait_for_connection(controller_idx)
    time.sleep(1)

    
    for i in range(500):
        nx.press_buttons(controller_idx, [Buttons.A])
        nx.press_buttons(controller_idx, [Buttons.R])
        print(f"Pressed A {i}")
 