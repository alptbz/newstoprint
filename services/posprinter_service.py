from textwrap import wrap
from typing import List
from escpos.printer import Network

_printer_address = ""

LINE_LENGTH = 48
LINE_BREAKER = "------------------------------------------------"


def init(printer_address):
    global _printer_address
    _printer_address = printer_address



def print_pos(print_lines: List[str], max=100):
    try:
        pos_printer = Network(_printer_address)
        i = 0
        for print_line in print_lines:
            if type(print_line) == str:
                if print_line == "-":
                    pos_printer.set(bold=True)
                    pos_printer.text(("-" * LINE_LENGTH) + "\n")
                elif print_line.startswith("{") or print_line.startswith("["):
                    pos_printer.set(bold=True, double_width=True, double_height=True)
                    pos_printer.text(print_line[1:] + "\n")
                    pos_printer.set(bold=True, double_width=False, double_height=False)
                else:
                    pos_printer.set(bold=True)
                    pos_printer.text(print_line + "\n")
            elif type(print_line) == dict:
                if print_line["type"] == "big":
                    pos_printer.set(bold=True, double_width=True, double_height=True)
                    pos_printer.text(print_line["text"] + "\n")
            i += 1
            if i > max:
                break
        pos_printer.print_and_feed()
        pos_printer.cut()
        pos_printer.close()
    except Exception as e:
        print("Pos Priting error")
        print(e)


def print_message(msg):
    lines = wrap(msg, width=48)
    lines.insert(0, LINE_BREAKER)
    lines.append(LINE_BREAKER)
    print_pos(lines)

