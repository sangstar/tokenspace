
# python wrapper for package wordspace/gosrc/tui within overall package tui
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy build -output=./tui ./gosrc/tui

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
try:
	import collections.abc as _collections_abc
except ImportError:
	_collections_abc = collections

cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
from . import _tui
from . import go

os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from tui import tui
# and then refer to everything using tui. prefix
# packages imported by this package listed below:




# ---- Types ---

# Python type for slice []*tui.CloseWord
class Slice_Ptr_tui_CloseWord(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tui.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tui.IncRef(self.handle)
		else:
			self.handle = _tui.Slice_Ptr_tui_CloseWord_CTor()
			_tui.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], _collections_abc.Iterable):
					raise TypeError('Slice_Ptr_tui_CloseWord.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_tui.DecRef(self.handle)
	def __str__(self):
		s = 'tui.Slice_Ptr_tui_CloseWord len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'tui.Slice_Ptr_tui_CloseWord([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _tui.Slice_Ptr_tui_CloseWord_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			if key.step == None or key.step == 1:
				st = key.start
				ed = key.stop
				if st == None:
					st = 0
				if ed == None:
					ed = _tui.Slice_Ptr_tui_CloseWord_len(self.handle)
				return Slice_Ptr_tui_CloseWord(handle=_tui.Slice_Ptr_tui_CloseWord_subslice(self.handle, st, ed))
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return CloseWord(handle=_tui.Slice_Ptr_tui_CloseWord_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_tui.Slice_Ptr_tui_CloseWord_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, _collections_abc.Iterable):
			raise TypeError('Slice_Ptr_tui_CloseWord.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = CloseWord(handle=_tui.Slice_Ptr_tui_CloseWord_elem(self.handle, self.index))
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_tui.Slice_Ptr_tui_CloseWord_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]

# Python type for slice []mat.Matrix
class Slice_mat_Matrix(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tui.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tui.IncRef(self.handle)
		else:
			self.handle = _tui.Slice_mat_Matrix_CTor()
			_tui.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], _collections_abc.Iterable):
					raise TypeError('Slice_mat_Matrix.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_tui.DecRef(self.handle)
	def __str__(self):
		s = 'tui.Slice_mat_Matrix len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'tui.Slice_mat_Matrix([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _tui.Slice_mat_Matrix_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			if key.step == None or key.step == 1:
				st = key.start
				ed = key.stop
				if st == None:
					st = 0
				if ed == None:
					ed = _tui.Slice_mat_Matrix_len(self.handle)
				return Slice_mat_Matrix(handle=_tui.Slice_mat_Matrix_subslice(self.handle, st, ed))
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return go.mat_Matrix(handle=_tui.Slice_mat_Matrix_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_tui.Slice_mat_Matrix_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, _collections_abc.Iterable):
			raise TypeError('Slice_mat_Matrix.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = go.mat_Matrix(handle=_tui.Slice_mat_Matrix_elem(self.handle, self.index))
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_tui.Slice_mat_Matrix_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---


# ---- Structs ---

# Python type for struct tui.Word
class Word(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tui.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tui.IncRef(self.handle)
		else:
			self.handle = _tui.tui_Word_CTor()
			_tui.IncRef(self.handle)
			if  0 < len(args):
				self.Name = args[0]
			if "Name" in kwargs:
				self.Name = kwargs["Name"]
			if  1 < len(args):
				self.Dim = args[1]
			if "Dim" in kwargs:
				self.Dim = kwargs["Dim"]
			if  2 < len(args):
				self.Vector = args[2]
			if "Vector" in kwargs:
				self.Vector = kwargs["Vector"]
			if  3 < len(args):
				self.Vector2D = args[3]
			if "Vector2D" in kwargs:
				self.Vector2D = kwargs["Vector2D"]
			if  4 < len(args):
				self.Idx = args[4]
			if "Idx" in kwargs:
				self.Idx = kwargs["Idx"]
	def __del__(self):
		_tui.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.Word{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.Word ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def Name(self):
		return _tui.tui_Word_Name_Get(self.handle)
	@Name.setter
	def Name(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Word_Name_Set(self.handle, value.handle)
		else:
			_tui.tui_Word_Name_Set(self.handle, value)
	@property
	def Dim(self):
		return _tui.tui_Word_Dim_Get(self.handle)
	@Dim.setter
	def Dim(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Word_Dim_Set(self.handle, value.handle)
		else:
			_tui.tui_Word_Dim_Set(self.handle, value)
	@property
	def Vector(self):
		return go.Slice_float64(handle=_tui.tui_Word_Vector_Get(self.handle))
	@Vector.setter
	def Vector(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Word_Vector_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	@property
	def Vector2D(self):
		return go.Slice_float64(handle=_tui.tui_Word_Vector2D_Get(self.handle))
	@Vector2D.setter
	def Vector2D(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Word_Vector2D_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	@property
	def Idx(self):
		return _tui.tui_Word_Idx_Get(self.handle)
	@Idx.setter
	def Idx(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Word_Idx_Set(self.handle, value.handle)
		else:
			_tui.tui_Word_Idx_Set(self.handle, value)

# Python type for struct tui.CloseWord
class CloseWord(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tui.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tui.IncRef(self.handle)
		else:
			self.handle = _tui.tui_CloseWord_CTor()
			_tui.IncRef(self.handle)
			if  0 < len(args):
				self.Word = args[0]
			if "Word" in kwargs:
				self.Word = kwargs["Word"]
			if  5 < len(args):
				self.Score = args[5]
			if "Score" in kwargs:
				self.Score = kwargs["Score"]
	def __del__(self):
		_tui.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.CloseWord{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.CloseWord ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def Word(self):
		return Word(handle=_tui.tui_CloseWord_Word_Get(self.handle))
	@Word.setter
	def Word(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_CloseWord_Word_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	@property
	def Score(self):
		return _tui.tui_CloseWord_Score_Get(self.handle)
	@Score.setter
	def Score(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_CloseWord_Score_Set(self.handle, value.handle)
		else:
			_tui.tui_CloseWord_Score_Set(self.handle, value)

# Python type for struct tui.ClosenessSet
class ClosenessSet(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tui.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tui.IncRef(self.handle)
		else:
			self.handle = _tui.tui_ClosenessSet_CTor()
			_tui.IncRef(self.handle)
			if  0 < len(args):
				self.CentralWord = args[0]
			if "CentralWord" in kwargs:
				self.CentralWord = kwargs["CentralWord"]
			if  1 < len(args):
				self.CloseWords = args[1]
			if "CloseWords" in kwargs:
				self.CloseWords = kwargs["CloseWords"]
	def __del__(self):
		_tui.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.ClosenessSet{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.ClosenessSet ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def CentralWord(self):
		return Word(handle=_tui.tui_ClosenessSet_CentralWord_Get(self.handle))
	@CentralWord.setter
	def CentralWord(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_ClosenessSet_CentralWord_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	@property
	def CloseWords(self):
		return Slice_Ptr_tui_CloseWord(handle=_tui.tui_ClosenessSet_CloseWords_Get(self.handle))
	@CloseWords.setter
	def CloseWords(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_ClosenessSet_CloseWords_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))

# Python type for struct tui.Result
class Result(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tui.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tui.IncRef(self.handle)
		else:
			self.handle = _tui.tui_Result_CTor()
			_tui.IncRef(self.handle)
			if  0 < len(args):
				self.FlattenedCompressed = args[0]
			if "FlattenedCompressed" in kwargs:
				self.FlattenedCompressed = kwargs["FlattenedCompressed"]
			if  1 < len(args):
				self.OriginalData = args[1]
			if "OriginalData" in kwargs:
				self.OriginalData = kwargs["OriginalData"]
			if  2 < len(args):
				self.Names = args[2]
			if "Names" in kwargs:
				self.Names = kwargs["Names"]
			if  3 < len(args):
				self.OutputDim = args[3]
			if "OutputDim" in kwargs:
				self.OutputDim = kwargs["OutputDim"]
			if  4 < len(args):
				self.N = args[4]
			if "N" in kwargs:
				self.N = kwargs["N"]
			if  5 < len(args):
				self.WindowSizeX = args[5]
			if "WindowSizeX" in kwargs:
				self.WindowSizeX = kwargs["WindowSizeX"]
			if  6 < len(args):
				self.WindowSizeY = args[6]
			if "WindowSizeY" in kwargs:
				self.WindowSizeY = kwargs["WindowSizeY"]
			if  7 < len(args):
				self.Alpha = args[7]
			if "Alpha" in kwargs:
				self.Alpha = kwargs["Alpha"]
			if  8 < len(args):
				self.NumWorkers = args[8]
			if "NumWorkers" in kwargs:
				self.NumWorkers = kwargs["NumWorkers"]
	def __del__(self):
		_tui.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.Result{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.Result ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def FlattenedCompressed(self):
		return Vectors(handle=_tui.tui_Result_FlattenedCompressed_Get(self.handle))
	@FlattenedCompressed.setter
	def FlattenedCompressed(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Result_FlattenedCompressed_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	@property
	def OriginalData(self):
		return Vectors(handle=_tui.tui_Result_OriginalData_Get(self.handle))
	@OriginalData.setter
	def OriginalData(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Result_OriginalData_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	@property
	def Names(self):
		return Ptr_Slice_string(handle=_tui.tui_Result_Names_Get(self.handle))
	@Names.setter
	def Names(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Result_Names_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	@property
	def OutputDim(self):
		return _tui.tui_Result_OutputDim_Get(self.handle)
	@OutputDim.setter
	def OutputDim(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Result_OutputDim_Set(self.handle, value.handle)
		else:
			_tui.tui_Result_OutputDim_Set(self.handle, value)
	@property
	def N(self):
		return _tui.tui_Result_N_Get(self.handle)
	@N.setter
	def N(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Result_N_Set(self.handle, value.handle)
		else:
			_tui.tui_Result_N_Set(self.handle, value)
	@property
	def WindowSizeX(self):
		return _tui.tui_Result_WindowSizeX_Get(self.handle)
	@WindowSizeX.setter
	def WindowSizeX(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Result_WindowSizeX_Set(self.handle, value.handle)
		else:
			_tui.tui_Result_WindowSizeX_Set(self.handle, value)
	@property
	def WindowSizeY(self):
		return _tui.tui_Result_WindowSizeY_Get(self.handle)
	@WindowSizeY.setter
	def WindowSizeY(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Result_WindowSizeY_Set(self.handle, value.handle)
		else:
			_tui.tui_Result_WindowSizeY_Set(self.handle, value)
	@property
	def Alpha(self):
		return _tui.tui_Result_Alpha_Get(self.handle)
	@Alpha.setter
	def Alpha(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Result_Alpha_Set(self.handle, value.handle)
		else:
			_tui.tui_Result_Alpha_Set(self.handle, value)
	@property
	def NumWorkers(self):
		return _tui.tui_Result_NumWorkers_Get(self.handle)
	@NumWorkers.setter
	def NumWorkers(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Result_NumWorkers_Set(self.handle, value.handle)
		else:
			_tui.tui_Result_NumWorkers_Set(self.handle, value)

# Python type for struct tui.ResultSet
class ResultSet(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tui.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tui.IncRef(self.handle)
		else:
			self.handle = _tui.tui_ResultSet_CTor()
			_tui.IncRef(self.handle)
	def __del__(self):
		_tui.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.ResultSet{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.ResultSet ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'

# Python type for struct tui.VecOpParams
class VecOpParams(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tui.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tui.IncRef(self.handle)
		else:
			self.handle = _tui.tui_VecOpParams_CTor()
			_tui.IncRef(self.handle)
	def __del__(self):
		_tui.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.VecOpParams{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.VecOpParams ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'

# Python type for struct tui.Vectors
class Vectors(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tui.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tui.IncRef(self.handle)
		else:
			self.handle = _tui.tui_Vectors_CTor()
			_tui.IncRef(self.handle)
			if  0 < len(args):
				self.Data = args[0]
			if "Data" in kwargs:
				self.Data = kwargs["Data"]
			if  1 < len(args):
				self.Rows = args[1]
			if "Rows" in kwargs:
				self.Rows = kwargs["Rows"]
			if  2 < len(args):
				self.Cols = args[2]
			if "Cols" in kwargs:
				self.Cols = kwargs["Cols"]
	def __del__(self):
		_tui.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.Vectors{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.Vectors ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def Data(self):
		return Ptr_Slice_float64(handle=_tui.tui_Vectors_Data_Get(self.handle))
	@Data.setter
	def Data(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Vectors_Data_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	@property
	def Rows(self):
		return _tui.tui_Vectors_Rows_Get(self.handle)
	@Rows.setter
	def Rows(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Vectors_Rows_Set(self.handle, value.handle)
		else:
			_tui.tui_Vectors_Rows_Set(self.handle, value)
	@property
	def Cols(self):
		return _tui.tui_Vectors_Cols_Get(self.handle)
	@Cols.setter
	def Cols(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_Vectors_Cols_Set(self.handle, value.handle)
		else:
			_tui.tui_Vectors_Cols_Set(self.handle, value)


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---
def DenseToVectors(m):
	"""DenseToVectors(object m) object"""
	return Vectors(handle=_tui.tui_DenseToVectors(m.handle))


# ---- Functions ---
def CompressAndVisualize(N, WindowSizeX, WindowSizeY, NumWorkers, Alpha, List, r, c, outputDim, Names):
	"""CompressAndVisualize(int N, int WindowSizeX, int WindowSizeY, int NumWorkers, float Alpha, []float List, int r, int c, int outputDim, []str Names) str"""
	return _tui.tui_CompressAndVisualize(N, WindowSizeX, WindowSizeY, NumWorkers, Alpha, List.handle, r, c, outputDim, Names.handle)
def Plot(xWindowSize, yWindowSize, closeSet):
	"""Plot(int xWindowSize, int yWindowSize, object closeSet) str"""
	return _tui.tui_Plot(xWindowSize, yWindowSize, closeSet.handle)
def Visualize(res):
	"""Visualize(object res) str"""
	return _tui.tui_Visualize(res.handle)


