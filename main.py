import time
from pynput import keyboard
from pynput.keyboard import Key, Controller

control = Controller()
invalid_keys = [Key.scroll_lock]
light_duration = 0.01

def valid(key):
	for invalid_key in invalid_keys:
		if key == invalid_key:
			return False
	return True

def toggle_light():
	control.press(Key.scroll_lock)
	control.release(Key.scroll_lock)
	
def on_release(key):
	if(not valid(key)): return
	toggle_light()
	time.sleep(light_duration)
	toggle_light()
	if key == Key.esc:
		return False

with keyboard.Listener(on_release=on_release) as listener:
	print("Tested only on Zeus k004\n\nListening for keyboard input...")
	listener.join()
