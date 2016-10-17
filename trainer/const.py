import sys


class _const(object):
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const(%s)" % name)
        self.__dict__[name] = value

    def __delattr__(self, name):
            if name in self.__dict__:
                raise self.ConstError("Can't unbind const(%s)" % name)
            raise NameError(name)
    categories = [
        ["1", "エンタメ"],
        ["2", "スポーツ"],
        ["3", "おもしろ"],
        ["4", "国内"],
        ["5", "海外"],
        ["6", "コラム"],
        ["7", "IT・科学"],
        ["8", "グルメ"]
    ]

sys.modules[__name__] = _const()
