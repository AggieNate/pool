import datetime

now = datetime.datetime.now()

print("\n**Pool Table Manager 1.0**\n\n----------------------\nPress RETURN to begin.\n----------------------")
input("")

class Table:
	def __init__(self, table_name, table_number):
		self.table_name = table_name
		self.table_number = table_number
		self.status = "Unoccupied"
		self.start_time = ""
		self.end_time = ""

table_1 = Table("Table 1", "1")
table_2 = Table("Table 2", "2")
table_3 = Table("Table 3", "3")
table_4 = Table("Table 4", "4")
table_5 = Table("Table 5", "5")
table_6 = Table("Table 6", "6")
table_7 = Table("Table 7", "7")
table_8 = Table("Table 8", "8")
table_9 = Table("Table 9", "9")
table_10 = Table("Table 10", "10")
table_11 = Table("Table 11", "11")
table_12 = Table("Table 12", "12")

tables = [table_1, table_2, table_3, table_4, table_5, table_6, table_7, table_8, table_9, table_10, table_11, table_12]

open_or_close = 0

start_time = " "

def display_table():
	for table in tables:
		if table.status == "Occupied":
			print(table.table_name + " -- " + table.status + " -- " + table.start_time)
		else:
			print(table.table_name + " -- " + table.status)

display_table()

def main():
	open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
	while open_or_close == "1":
		table_to_open = input("\nWhich table would you like to open?\n>> ")
		if table_1.status == "Occupied" and table_to_open == "1":
			print("\n** TABLE ALAREADY OCCUPIED. **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_1.status != "Occupied" and table_to_open == "1":
			table_1.status = "Occupied"
			table_1.start_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_2.status == "Occupied" and table_to_open == "2":
			print("\n** TABLE ALREADY OCCUPIED **\n")
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_2.status != "Occupied" and table_to_open == "2":
			table_2.status = "Occupied"
			table_2.start_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_3.status == "Occupied" and table_to_open == "3":
			print("\n** TABLE ALREADY OCCUPIED. ** \n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>>")
		elif table_3.status != "Occupied" and table_to_open == "3":
			table_3.status = "Occupied"
			table_3.start_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_4.status == "Occupied" and table_to_open == "4":
			print("\n** TABLE ALAREADY OCCUPIED. **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_4.status != "Occupied" and table_to_open == "4":
			table_4.status = "Occupied"
			table_4.start_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_5.status == "Occupied" and table_to_open == "5":
			print("\n** TABLE ALAREADY OCCUPIED. **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_5.status != "Occupied" and table_to_open == "5":
			table_5.status = "Occupied"
			table_5.start_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_6.status == "Occupied" and table_to_open == "6":
			print("\n** TABLE ALAREADY OCCUPIED. **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_6.status != "Occupied" and table_to_open == "6":
			table_6.status = "Occupied"
			table_6.start_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_7.status == "Occupied" and table_to_open == "7":
			print("\n** TABLE ALAREADY OCCUPIED. **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_7.status != "Occupied" and table_to_open == "7":
			table_7.status = "Occupied"
			table_7.start_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_8.status == "Occupied" and table_to_open == "8":
			print("\n** TABLE ALREADY OCCUPIED **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_8.status != "Occupied" and table_to_open == "8":
			table_8.status = "Occupied"
			table_8.start_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_9.status == "Occupied" and table_to_open == "9":
			print("\n** TABLE ALREADY OCCUPIED. ** \n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>>")
		elif table_9.status != "Occupied" and table_to_open == "9":
			table_9.status = "Occupied"
			table_1.start_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_10.status == "Occupied" and table_to_open == "10":
			print("\n** TABLE ALAREADY OCCUPIED. **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_10.status != "Occupied" and table_to_open == "10":
			table_10.status = "Occupied"
			table_10.start_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_11.status == "Occupied" and table_to_open == "11":
			print("\n** TABLE ALAREADY OCCUPIED. **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_11.status != "Occupied" and table_to_open == "11":
			table_11.status = "Occupied"
			table_11.start_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_12.status == "Occupied" and table_to_open == "12":
			print("\n** TABLE ALAREADY OCCUPIED. **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_12.status != "Occupied" and table_to_open == "12":
			table_12.status = "Occupied"
			table_12.start_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")

	while open_or_close == "2":
		table_to_close = input("\nWhich table would you like to close?\n>> ")
		if table_1.status == "Unoccupied" and table_to_close == "1":
			print("\n** YOU CANNOT CLOSE AN UNOCCUPIED TABLE **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_1.status != "Unoccupied" and table_to_close == "1":
			table_1.status = "Unoccupied"
			table_1.end_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_2.status == "Unoccupied" and table_to_close == "2":
			print("\n** YOU CANNOT CLOSE AN UNOCCUPIED TABLE **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_2.status != "Unoccupied" and table_to_close == "2":
			table_2.status = "Unoccupied"
			table_2.end_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_3.status == "Unoccupied" and table_to_close == "3":
			print("\n** YOU CANNOT CLOSE AN UNOCCUPIED TABLE **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_3.status != "Unoccupied" and table_to_close == "3":
			table_3.status = "Unoccupied"
			table_3.end_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_4.status == "Unoccupied" and table_to_close == "4":
			print("\n** YOU CANNOT CLOSE AN UNOCCUPIED TABLE **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_4.status != "Unoccupied" and table_to_close == "4":
			table_4.status = "Unoccupied"
			table_4.end_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_5.status == "Unoccupied" and table_to_close == "5":
			print("\n** YOU CANNOT CLOSE AN UNOCCUPIED TABLE **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_5.status != "Unoccupied" and table_to_close == "5":
			table_5.status = "Unoccupied"
			table_5.end_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_6.status == "Unoccupied" and table_to_close == "6":
			print("\n** YOU CANNOT CLOSE AN UNOCCUPIED TABLE **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_6.status != "Unoccupied" and table_to_close == "6":
			table_6.status = "Unoccupied"
			table_6.end_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_7.status == "Unoccupied" and table_to_close == "7":
			print("\n** YOU CANNOT CLOSE AN UNOCCUPIED TABLE **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_7.status != "Unoccupied" and table_to_close == "7":
			table_7.status = "Unoccupied"
			table_7.end_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_8.status == "Unoccupied" and table_to_close == "8":
			print("\n** YOU CANNOT CLOSE AN UNOCCUPIED TABLE **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_8.status != "Unoccupied" and table_to_close == "8":
			table_8.status = "Unoccupied"
			table_8.end_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_9.status == "Unoccupied" and table_to_close == "9":
			print("\n** YOU CANNOT CLOSE AN UNOCCUPIED TABLE **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_9.status != "Unoccupied" and table_to_close == "9":
			table_9.status = "Unoccupied"
			table_9.end_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_10.status == "Unoccupied" and table_to_close == "10":
			print("\n** YOU CANNOT CLOSE AN UNOCCUPIED TABLE **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_10.status != "Unoccupied" and table_to_close == "10":
			table_10.status = "Unoccupied"
			table_10.end_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_11.status == "Unoccupied" and table_to_close == "11":
			print("\n** YOU CANNOT CLOSE AN UNOCCUPIED TABLE **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_11.status != "Unoccupied" and table_to_close == "11":
			table_11.status = "Unoccupied"
			table_11.end_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_12.status == "Unoccupied" and table_to_close == "12":
			print("\n** YOU CANNOT CLOSE AN UNOCCUPIED TABLE **\n")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")
		elif table_12.status != "Unoccupied" and table_to_close == "12":
			table_12.status = "Unoccupied"
			table_12.end_time = now.strftime("%Y-%m-%d %H:%M")
			display_table()
			open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")

main()
display_table()
open_or_close = input("\nPress 1 to open a table. Press 2 to close a table.\n1. Open Table\n2. Close Table\n>> ")


