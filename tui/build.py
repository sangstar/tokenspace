# python build stubs for package tui
# File is generated by gopy. Do not edit.
# gopy build -output=./tui ./gosrc/tui

from pybindgen import retval, param, Function, Module
import sys

class CheckedFunction(Function):
    def __init__(self, *a, **kw):
        super(CheckedFunction, self).__init__(*a, **kw)
        self._failure_expression = kw.get('failure_expression', '')
        self._failure_cleanup = kw.get('failure_cleanup', '')

    def set_failure_expression(self, expr):
        self._failure_expression = expr

    def set_failure_cleanup(self, expr):
        self._failure_cleanup = expr

    def generate_call(self):
        super(CheckedFunction, self).generate_call()
        check = "PyErr_Occurred()"
        if self._failure_expression:
            check = "{} && {}".format(self._failure_expression, check)
        failure_cleanup = self._failure_cleanup or None
        self.before_call.write_error_check(check, failure_cleanup)

def add_checked_function(mod, name, retval, params, failure_expression='', *a, **kw):
    fn = CheckedFunction(name, retval, params, *a, **kw)
    fn.set_failure_expression(failure_expression)
    mod._add_function_obj(fn)
    return fn

def add_checked_string_function(mod, name, retval, params, failure_expression='', *a, **kw):
    fn = CheckedFunction(name, retval, params, *a, **kw)
    fn.set_failure_cleanup('if (retval != NULL) free(retval);')
    fn.after_call.add_cleanup_code('free(retval);')
    fn.set_failure_expression(failure_expression)
    mod._add_function_obj(fn)
    return fn

mod = Module('_tui')
mod.add_include('"tui_go.h"')
mod.add_function('GoPyInit', None, [])
mod.add_function('DecRef', None, [param('int64_t', 'handle')])
mod.add_function('IncRef', None, [param('int64_t', 'handle')])
mod.add_function('NumHandles', retval('int'), [])
mod.add_function('Slice_bool_CTor', retval('int64_t'), [])
mod.add_function('Slice_bool_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_bool_elem', retval('bool'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_bool_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_bool_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('bool', 'value')])
mod.add_function('Slice_bool_append', None, [param('int64_t', 'handle'), param('bool', 'value')])
mod.add_function('Slice_byte_CTor', retval('int64_t'), [])
mod.add_function('Slice_byte_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_byte_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_byte_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_byte_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Slice_byte_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('Slice_byte_from_bytes', retval('int64_t'), [param('PyObject*', 'o', transfer_ownership=False)])
mod.add_function('Slice_byte_to_bytes', retval('PyObject*', caller_owns_return=True), [param('int64_t', 'handle')])
mod.add_function('Slice_error_CTor', retval('int64_t'), [])
mod.add_function('Slice_error_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_error_elem', retval('char*'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_error_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_error_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('char*', 'value')])
mod.add_function('Slice_error_append', None, [param('int64_t', 'handle'), param('char*', 'value')])
mod.add_function('Slice_float32_CTor', retval('int64_t'), [])
mod.add_function('Slice_float32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_float32_elem', retval('float'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_float32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_float32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('float', 'value')])
mod.add_function('Slice_float32_append', None, [param('int64_t', 'handle'), param('float', 'value')])
mod.add_function('Slice_float64_CTor', retval('int64_t'), [])
mod.add_function('Slice_float64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_float64_elem', retval('double'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_float64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_float64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('double', 'value')])
mod.add_function('Slice_float64_append', None, [param('int64_t', 'handle'), param('double', 'value')])
mod.add_function('Slice_int_CTor', retval('int64_t'), [])
mod.add_function('Slice_int_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_int_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_int16_CTor', retval('int64_t'), [])
mod.add_function('Slice_int16_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int16_elem', retval('int16_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int16_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int16_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int16_t', 'value')])
mod.add_function('Slice_int16_append', None, [param('int64_t', 'handle'), param('int16_t', 'value')])
mod.add_function('Slice_int32_CTor', retval('int64_t'), [])
mod.add_function('Slice_int32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int32_elem', retval('int32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int32_t', 'value')])
mod.add_function('Slice_int32_append', None, [param('int64_t', 'handle'), param('int32_t', 'value')])
mod.add_function('Slice_int64_CTor', retval('int64_t'), [])
mod.add_function('Slice_int64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int64_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_int64_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_int8_CTor', retval('int64_t'), [])
mod.add_function('Slice_int8_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int8_elem', retval('int8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int8_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int8_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int8_t', 'value')])
mod.add_function('Slice_int8_append', None, [param('int64_t', 'handle'), param('int8_t', 'value')])
mod.add_function('Slice_rune_CTor', retval('int64_t'), [])
mod.add_function('Slice_rune_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_rune_elem', retval('int32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_rune_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_rune_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int32_t', 'value')])
mod.add_function('Slice_rune_append', None, [param('int64_t', 'handle'), param('int32_t', 'value')])
mod.add_function('Slice_string_CTor', retval('int64_t'), [])
mod.add_function('Slice_string_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_string_elem', retval('char*'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_string_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_string_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('char*', 'value')])
mod.add_function('Slice_string_append', None, [param('int64_t', 'handle'), param('char*', 'value')])
mod.add_function('Slice_uint_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint_elem', retval('uint64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint64_t', 'value')])
mod.add_function('Slice_uint_append', None, [param('int64_t', 'handle'), param('uint64_t', 'value')])
mod.add_function('Slice_uint16_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint16_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint16_elem', retval('uint16_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint16_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint16_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint16_t', 'value')])
mod.add_function('Slice_uint16_append', None, [param('int64_t', 'handle'), param('uint16_t', 'value')])
mod.add_function('Slice_uint32_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint32_elem', retval('uint32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint32_t', 'value')])
mod.add_function('Slice_uint32_append', None, [param('int64_t', 'handle'), param('uint32_t', 'value')])
mod.add_function('Slice_uint64_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint64_elem', retval('uint64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint64_t', 'value')])
mod.add_function('Slice_uint64_append', None, [param('int64_t', 'handle'), param('uint64_t', 'value')])
mod.add_function('Slice_uint8_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint8_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint8_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint8_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint8_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Slice_uint8_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('Slice_Ptr_tui_CloseWord_CTor', retval('int64_t'), [])
mod.add_function('Slice_Ptr_tui_CloseWord_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_Ptr_tui_CloseWord_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_Ptr_tui_CloseWord_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_Ptr_tui_CloseWord_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_Ptr_tui_CloseWord_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_mat_Matrix_CTor', retval('int64_t'), [])
mod.add_function('Slice_mat_Matrix_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_mat_Matrix_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_mat_Matrix_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_mat_Matrix_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_mat_Matrix_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('tui_Word_CTor', retval('int64_t'), [])
mod.add_function('tui_Word_Name_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('tui_Word_Name_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('tui_Word_Dim_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Word_Dim_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_Word_Vector_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Word_Vector_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_Word_Vector2D_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Word_Vector2D_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_Word_Idx_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Word_Idx_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_CloseWord_CTor', retval('int64_t'), [])
mod.add_function('tui_CloseWord_Word_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_CloseWord_Word_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_CloseWord_Score_Get', retval('double'), [param('int64_t', 'handle')])
mod.add_function('tui_CloseWord_Score_Set', None, [param('int64_t', 'handle'), param('double', 'val')])
mod.add_function('tui_ClosenessSet_CTor', retval('int64_t'), [])
mod.add_function('tui_ClosenessSet_CentralWord_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_ClosenessSet_CentralWord_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_ClosenessSet_CloseWords_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_ClosenessSet_CloseWords_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_Result_CTor', retval('int64_t'), [])
mod.add_function('tui_Result_FlattenedCompressed_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Result_FlattenedCompressed_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_Result_OriginalData_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Result_OriginalData_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_Result_Names_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Result_Names_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_Result_OutputDim_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Result_OutputDim_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_Result_N_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Result_N_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_Result_WindowSizeX_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Result_WindowSizeX_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_Result_WindowSizeY_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Result_WindowSizeY_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_Result_Alpha_Get', retval('double'), [param('int64_t', 'handle')])
mod.add_function('tui_Result_Alpha_Set', None, [param('int64_t', 'handle'), param('double', 'val')])
mod.add_function('tui_Result_NumWorkers_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Result_NumWorkers_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_ResultSet_CTor', retval('int64_t'), [])
mod.add_function('tui_VecOpParams_CTor', retval('int64_t'), [])
mod.add_function('tui_Vectors_CTor', retval('int64_t'), [])
mod.add_function('tui_Vectors_Data_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Vectors_Data_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_Vectors_Rows_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Vectors_Rows_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('tui_Vectors_Cols_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('tui_Vectors_Cols_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
add_checked_function(mod, 'tui_DenseToVectors', retval('int64_t'), [param('int64_t', 'm')])
add_checked_function(mod, 'tui_CompressAndVisualize', retval('char*'), [param('int64_t', 'N'), param('int64_t', 'WindowSizeX'), param('int64_t', 'WindowSizeY'), param('int64_t', 'NumWorkers'), param('double', 'Alpha'), param('int64_t', 'List'), param('int64_t', 'r'), param('int64_t', 'c'), param('int64_t', 'outputDim'), param('int64_t', 'Names')])
add_checked_string_function(mod, 'tui_Plot', retval('char*'), [param('int64_t', 'xWindowSize'), param('int64_t', 'yWindowSize'), param('int64_t', 'closeSet')])
add_checked_function(mod, 'tui_Visualize', retval('char*'), [param('int64_t', 'res')])

mod.generate(open('tui.c', 'w'))

