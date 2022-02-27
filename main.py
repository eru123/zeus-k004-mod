from pynput import keyboard
from pynput.keyboard import Key, Controller

control = Controller()
invalid_keys = [Key.scroll_lock]

def valid(key):
	for invalid_key in invalid_keys:
		if key == invalid_key:
			return False
	return True

def toggle_light():
	control.press(Key.scroll_lock)
	control.release(Key.scroll_lock)

def on_press(key):
	if(not valid(key)): return
	toggle_light()
	
def on_release(key):
	if(not valid(key)): return
	toggle_light()
	if key == Key.esc:
		return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	print("Listening for keyboard input...")
	listener.join()
