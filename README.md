dicttools
---------

a set of dictionary utilities that attempt to make handling python dictionaries
a little easier. 

installing
----------

> git clone http://github.com/rlgomes/dicttools.git#egg=dicttools
> cd dicttools
> python setup.py install

or install directly from github with:

> pip install -e git+git://github.com/rlgomes/dicttools.git#egg=dicttools

usage
-----

```{r basicconsole}
> import dicttools
> dicttools.filter(lambda key, value: key > 2, { 1: None, 2:{ 3: None }, 4:{}})
{4: {}}
```

```{r basicconsole}
> dicttools.map(lambda key, value: (key, True), { 1: None, 2: 23, 4:{}})
{1: True, 2: True, 4: True}
```

