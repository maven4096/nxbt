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
            adapter_path=adapters[i])
            #colour_body=[255,255,255],
            #colour_buttons=[255,255,255])
        controller_idxs.append(index)

    # Select the last controller for input
    controller_idx = controller_idxs[-1]

    nx.wait_for_connection(controller_idx)
    time.sleep(2)

    #Step 1
    nx.press_buttons(controller_idx, [Buttons.A])
    time.sleep(2)

    #Step 2
    nx.press_buttons(controller_idx, [Buttons.B])
    time.sleep(2)
    
    #Step 3
    nx.press_buttons(controller_idx, [Buttons.DPAD_UP])
    time.sleep(2)

    #Step 4
    nx.press_buttons(controller_idx, [Buttons.DPAD_LEFT])
    time.sleep(2)

    #Step 5
    nx.press_buttons(controller_idx, [Buttons.DPAD_LEFT])
    time.sleep(2)

    #Step 6
    nx.press_buttons(controller_idx, [Buttons.A])
    time.sleep(2)

    for i in range(10000):
        nx.press_buttons(controller_idx, [Buttons.A])

    print("Exiting...")
