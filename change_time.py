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
    time.sleep(2)

    #Step 1
    #nx.press_buttons(controller_idx, [Buttons.Y])
    #print("Pressed Y")
    #time.sleep(0.5)

    nx.press_buttons(controller_idx, [Buttons.HOME])
    print("Pressed HOME")
    time.sleep(0.5)

    nx.press_buttons(controller_idx, [Buttons.DPAD_DOWN])
    print("Pressed DPAD_DOWN")
    time.sleep(0.5)

    for i in range(7):
        nx.press_buttons(controller_idx, [Buttons.DPAD_RIGHT])
        print(f"Pressed DPAD_RIGHT {i}")     
        time.sleep(0.5)

    nx.press_buttons(controller_idx, [Buttons.A])
    print("Pressed A")
    time.sleep(0.5)

    for i in range(15):
        nx.press_buttons(controller_idx, [Buttons.DPAD_DOWN])
        print("Pressed DPAD_DOWN")
        time.sleep(0.5)

    nx.press_buttons(controller_idx, [Buttons.DPAD_RIGHT])
    print("Pressed DPAD_RIGHT")
    time.sleep(0.5)

    for i in range(9):
        nx.press_buttons(controller_idx, [Buttons.DPAD_DOWN])
        print("Pressed DPAD_DOWN")
        time.sleep(0.5)

    nx.press_buttons(controller_idx, [Buttons.A])
    print("Pressed A")
    time.sleep(0.5)

    nx.press_buttons(controller_idx, [Buttons.DPAD_DOWN])
    print("Pressed DPAD_DOWN")
    time.sleep(0.5)

    nx.press_buttons(controller_idx, [Buttons.DPAD_DOWN])
    nx.press_buttons(controller_idx, [Buttons.DPAD_DOWN])
    print("Pressed DPAD_DOWN")
    time.sleep(0.5)

    nx.press_buttons(controller_idx, [Buttons.A])
    print("Pressed A")
    time.sleep(0.5)

    nx.press_buttons(controller_idx, [Buttons.DPAD_RIGHT])
    print("Pressed DPAD_RIGHT") 
    time.sleep(0.5)

    nx.press_buttons(controller_idx, [Buttons.DPAD_UP])
    print("Pressed DPAD_UP")
    time.sleep(0.5)

    nx.press_buttons(controller_idx, [Buttons.DPAD_UP])
    print("Pressed DPAD_UP")
    time.sleep(0.5)

    for i in range(5):
        nx.press_buttons(controller_idx, [Buttons.DPAD_RIGHT])
        print("Pressed DPAD_RIGHT")
        time.sleep(0.5)

    nx.press_buttons(controller_idx, [Buttons.A])
    print("Pressed A")
    time.sleep(0.5)

    nx.press_buttons(controller_idx, [Buttons.HOME])
    print("Pressed HOME")
    time.sleep(0.5)

    nx.press_buttons(controller_idx, [Buttons.A])
    print("Pressed A")
    time.sleep(0.5)


