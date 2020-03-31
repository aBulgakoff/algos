def property_factory(field_name):
    _field_name = f'_{field_name}'

    def getter(self):
        if _field_name in self.__dict__:
            return getattr(self, _field_name)

    def setter_once(self, value):
        # sets only if no value set
        if not getter(self):
            setattr(self, _field_name, value)

    return property(getter, setter_once)


class Context:
    def __repr__(self) -> str:
        return f'Client Context ID:{id(self)} {self.__dict__}'


def set_immutable_data(data_class, data_obj, key, value):
    # set properties to Class fields:
    setattr(data_class, key, property_factory(key))
    # set values to Instance fields:
    setattr(data_obj, key, value)


if __name__ == '__main__':
    overridden_data = {'date': 20202020, 'place': 'AMER'}
    cx = Context()

    for key, value in overridden_data.items():
        set_immutable_data(Context, cx, key, value)

    # Testing if it works:
    # instance after setting fields
    print(f'Overridden data: {cx}')
    # Try to change fields
    cx.date, cx.place = 'EURO', 19990101
    # overridden fields stays in instance
    print(f'During test execution: {cx}')
