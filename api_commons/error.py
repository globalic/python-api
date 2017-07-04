#    Boilerplate commons for django based web api application.
#    Copyright (C) 2017 Logicify
#    The MIT License (MIT)
#    
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction,
#    including without limitation the rights to use, copy, modify, merge,
#    publish, distribute, sublicense, and/or sell copies of the Software,
#    and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#    
#    The above copyright notice and this permission notice shall be
#    included in all copies or substantial portions of the Software.
#    
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

class InvalidInputDataError(Exception):
    def __init__(self, msg, input_value, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
        self.input_value = input_value


class InvalidPaginationOptionsError(Exception):
    pass


class NotFoundException(Exception):
    def __init__(self, msg, input_value, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
        self.input_value = input_value


class ErrorCode:
    def __init__(self, error_code, dto_or_error_message=''):
        self.error_code = error_code
        self.dto_or_error_message = dto_or_error_message