import os.path
import sys
import PP1_9

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP1_9.py")
		assert exists
	except:
		sys.exit()

	PP1_9.q1()
	captured = capsys.readouterr()
	assert captured.out == '"Hello World"\n'

def test_q2_1(capsys):

	try:
		exists = os.path.exists("PP1_9.py")
		assert exists
	except:
		sys.exit()

	input_values = ['teSt']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_9.input = mock_input

	PP1_9.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a word: test\nTEST\n"

def test_q3_1(capsys):

	try:
		exists = os.path.exists("PP1_9.py")
		assert exists
	except:
		sys.exit()

	input_values = ['very long word']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_9.input = mock_input

	PP1_9.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input a word that is at least 5 letters long: ery\n"

def test_q4_1(capsys):

	try:
		exists = os.path.exists("PP1_9.py")
		assert exists
	except:
		sys.exit()

	input_values = ['bellows']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_9.input = mock_input

	PP1_9.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input a word: 4\n"

def test_q5_1(capsys):

	try:
		exists = os.path.exists("PP1_9.py")
		assert exists
	except:
		sys.exit()

	input_values = ['bye']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_9.input = mock_input

	PP1_9.q5()
	captured = capsys.readouterr()
	assert captured.out == "Input a word: 3\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP1_9.py")
		assert exists
	except:
		sys.exit()

	PP1_9.q1()
	captured = capsys.readouterr()
	assert captured.out == '"Hello World"\n'

def test_q2_2(capsys):

	try:
		exists = os.path.exists("PP1_9.py")
		assert exists
	except:
		sys.exit()

	input_values = ['helLo']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_9.input = mock_input

	PP1_9.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a word: hello\nHELLO\n"

def test_q3_2(capsys):

	try:
		exists = os.path.exists("PP1_9.py")
		assert exists
	except:
		sys.exit()

	input_values = ['snake']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_9.input = mock_input

	PP1_9.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input a word that is at least 5 letters long: nak\n"

def test_q4_2(capsys):

	try:
		exists = os.path.exists("PP1_9.py")
		assert exists
	except:
		sys.exit()

	input_values = ['bobby']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_9.input = mock_input

	PP1_9.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input a word: 1\n"

def test_q5_2(capsys):

	try:
		exists = os.path.exists("PP1_9.py")
		assert exists
	except:
		sys.exit()

	input_values = ['a bunch of gibberish']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_9.input = mock_input

	PP1_9.q5()
	captured = capsys.readouterr()
	assert captured.out == "Input a word: 20\n"

