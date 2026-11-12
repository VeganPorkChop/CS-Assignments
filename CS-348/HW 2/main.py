import common
import student_code

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"

def check_result(sudoku, show):
	result=True
	for y in range(9):
		v=""
		for x in range(9):
			value = sudoku[y][x];
			sudoku[y][x]=0
			if (value!=0 and common.can_yx_be_z(sudoku,y,x,value)):
				v+=bcolors.GREEN
			else:
				result = False
				v+=bcolors.RED
			v+=str(value)
			sudoku[y][x]=value
		if (show):
			print(v)
	return result

def check_clues(sudoku, data):
	"""Cells that started with a value other than 0 must not be changed."""
	for y in range(9):
		for x in range(9):
			given = int(data[y*9+x])
			if (given!=0 and sudoku[y][x]!=given):
				return False
	return True

def report(label, sudoku, data, count, limit):
	"""Check one algorithm's board and count. Returns True if both are right."""
	result=True

	if (not check_result(sudoku,False)):
		print(label+" results: "+bcolors.RED+"FAIL"+bcolors.NORMAL)
		check_result(sudoku,True)
		result=False
	elif (not check_clues(sudoku,data)):
		print(label+" results: "+bcolors.RED+"FAIL (cells that started non-zero were changed)"+bcolors.NORMAL)
		check_result(sudoku,True)
		result=False
	else:
		print(label+" results: "+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL)

	if (count!=limit):
		print(label+" count: "+str(count)+" (expected "+str(limit)+") ("+bcolors.RED+"FAIL"+bcolors.NORMAL+")")
		result=False
	else:
		print(label+" count: "+str(count)+" ("+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL+")")

	return result

def run_experiment(data, btlimit, fclimit):
	sudoku = common.init_sudoku()
	common.set_sudoku(sudoku, data)
	bt1 = student_code.sudoku_backtracking(sudoku)
	ok_bt = report("Backtracking", sudoku, data, bt1, btlimit)

	common.set_sudoku(sudoku, data)
	fc1 = student_code.sudoku_forwardchecking(sudoku)
	ok_fc = report("Forwardchecking", sudoku, data, fc1, fclimit)

	return ok_bt and ok_fc


data1 = ("900670000"
"006800470"
"800010003"
"003000001"
"005406900"
"600000300"
"300060008"
"068005200"
"000082006")

data2 = ("006100050"
"200605008"
"000090002"
"000019300"
"002000800"
"003570000"
"900040000"
"800301009"
"040006100")

data3 = ("530070000"
"600195000"
"098000060"
"800060003"
"400803001"
"700020006"
"060000280"
"000419005"
"000080079")

data4 = ("009000400"
"600400020"
"840031090"
"008007041"
"500060003"
"160800700"
"070290065"
"020005004"
"005000900")

data5 = ("295831467"
"846275913"
"371694852"
"014082396"
"630410528"
"082060174"
"160000200"
"458926731"
"020100600")


data6 = ("921786453"
"786453921"
"543912867"
"839671245"
"162549738"
"475328196"
"214835679"
"398267514"
"657194382")


BOARDS = [
	("Board 1", data1, 3448, 1078),
	("Board 2", data2, 21819, 2815),
	("Board 3", data3, 4209, 334),
	("Board 4", data4, 655, 235),
	("Board 5", data5, 22, 20),
	("Board 6", data6, 1, 1),
]


def main():
	results = []
	for name, data, btlimit, fclimit in BOARDS:
		print(name)
		results.append(run_experiment(data, btlimit, fclimit))

	passed = sum(1 for r in results if r)
	print("")
	print("Boards fully passed: "+str(passed)+" of "+str(len(BOARDS)))
	for (name, _, _, _), ok in zip(BOARDS, results):
		if not ok:
			print("  "+bcolors.RED+"FAILED"+bcolors.NORMAL+": "+name)

	return 0 if all(results) else 1


if __name__ == "__main__":
	exit(main())
