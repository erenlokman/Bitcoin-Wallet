import curses
import time
import electrum
import os


menu = ['Create Address', 'Check Balance', 'Send Bitcoin', 'Exit']

def print_menu(stdscr, selected_row_idx):

	stdscr.clear()

	h, w = stdscr.getmaxyx()
	
	for idx, row in enumerate(menu):
		x = w // 2 - len(row) // 2
		y = h // 2 - len(menu) // 2 + idx
		
		if idx == selected_row_idx:
			stdscr.attron(curses.color_pair(1))
			stdscr.addstr(y,x,row)
			stdscr.attroff(curses.color_pair(1))
		else:
			stdscr.addstr(y,x,row)
			
	stdscr.refresh()
	
def create_address(stdscr):

	stdscr.clear()
	
	h, w = stdscr.getmaxyx()
	
	text = 'The new address has been created = ' + os.popen("./run_electrum --testnet createnewaddress").read()
	x = w // 2 - len(text) // 2
	y = h // 2
	
	stdscr.addstr(y,x,text)
	
def check_balance(stdscr):

	stdscr.clear()
		
	h, w = stdscr.getmaxyx()
	
	text = 'Balance = ' + os.popen("./run_electrum --testnet getbalance").read()
	x = w // 2 - len(text) // 2
	y = h // 2
	
	stdscr.addstr(y,x,text)
	
def send_bitcoin(stdscr):

	stdscr.clear()
		
	h, w = stdscr.getmaxyx()
	
	text = 'Enter the address & Amount = ' + (os.popen("./run_electrum --testnet payto tb1qm5tfegjevj27yvvna9elym9lnzcf0zraxgl8z2 0.000001").read() + + os.popen("./run_electrum --testnet payto tb1qm5tfegjevj27yvvna9elym9lnzcf0zraxgl8z2 0.000001").read())
	x = w // 2 - len(text) // 2
	y = h // 2
	
	stdscr.addstr(y,x,text)
	

	
def main(stdscr):
	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	
	current_row_idx = 0
	
	print_menu(stdscr, current_row_idx)

	send_bitcoin(stdscr)
	while 1:
		key = stdscr.getch()
		
		stdscr.clear()
		
		if key == curses.KEY_UP and current_row_idx > 0:
			current_row_idx -= 1

		elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
			current_row_idx += 1

		elif key == curses.KEY_ENTER or key in [10,13]:
			stdscr.addstr(0,0, "You pressed {}".format(menu[current_row_idx]))
			stdscr.refresh()
			stdscr.getch()
			
			if current_row_idx == len(menu)-1:
				break
		
		print_menu(stdscr, current_row_idx)	
		stdscr.refresh()
	

curses.wrapper(main)
