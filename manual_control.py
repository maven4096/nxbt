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

        controller_idxs.append(index)

    # Select the last controller for input
    controller_idx = controller_idxs[-1]

    nx.wait_for_connection(controller_idx)
    

    def controller_input(key):
        if key == 'a':
            nx.press_buttons(controller_idx, [Buttons.A])
        elif key == 'b':
            nx.press_buttons(controller_idx, [Buttons.B])
        elif key == 'x':
            nx.press_buttons(controller_idx, [Buttons.X])
        elif key == 'y':
            nx.press_buttons(controller_idx, [Buttons.Y])
        elif key == 'w':
            nx.press_buttons(controller_idx, [Buttons.DPAD_UP])
        elif key == 's':
            nx.press_buttons(controller_idx, [Buttons.DPAD_DOWN])
        elif key == 'q':
            nx.press_buttons(controller_idx, [Buttons.DPAD_LEFT])
        elif key == 'e':
            nx.press_buttons(controller_idx, [Buttons.DPAD_RIGHT])
        elif key == 'h':
            nx.press_buttons(controller_idx, [Buttons.HOME])

    while True:
        key = input("Press a key (a, b, x, y, up, down, left, right) or 'exit' to quit: ").strip().lower().split()
        if key in ['up', 'down', 'left', 'right', 'home']:
            controller_input(key)
            continue
        for i in key:
            if i == 'exit':
                print("Exiting...")
                break
            elif i in ['a', 'b', 'x', 'y', 'w', 's', 'q', 'e', 'h']:
                controller_input(i)
            else:
                print("Invalid key. Please try again.")
            time.sleep(1)  # Add a delay to avoid flooding the input
        