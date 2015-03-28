## Yet Another (Pythonic) XML Library ##

[YAXL](http://code.google.com/p/yaxl) is a library for reading, writing and manipulating [XML](http://www.w3.org/TR/REC-xml/) in [Python](http://www.python.org/). It is **OSI Certified Open Source Software** released under the MIT License. This means you are free to download it and do (almost) whatever you want with it.

&lt;wiki:gadget url="http://www.ohloh.net/p/315772/widgets/project\_basic\_stats.xml" height="220" style="float: right" border="1" /&gt;

### Requirements ###

  * [Python](http://www.python.org) version 2.4 or higher

### Features ###

  * Requires only Python 2.4+
  * Learnable in 15 minutes
  * Simplest interface possible - minimal number of functions and objects exported
  * [XML Namespace](http://www.w3.org/TR/REC-xml-names) aware
  * [XPath](http://www.w3.org/TR/xpath) support
  * Easy to create [XML](http://www.w3.org/TR/REC-xml/) documents **and** fragments
  * Easy to read in and manipulate [XML](http://www.w3.org/TR/REC-xml/) documents **and** fragments

### Usage ###

[Developing with YAXL](http://code.google.com/p/yaxl/wiki/YAXLOverview) is a tutorial that should get you started using YAXL as quickly as possible. I have put a lot of time and effort into documenting YAXL; so if there is anything that needs more explanation or is not clear for some reason, please let me know.

Use code like the following to access the module's built-in help:

```
>>> import yaxl
>>> help(yaxl)
```

### Why another XML library? Especially for Python? ###

I looked around (even spent some time sifting through Uche Ogbuji's
[State of Python-XML in 2004](http://www.xml.com/pub/a/2004/10/13/py-xml.html) with its 74 projects) and couldn't find anything I liked. The existing modules were all "un-Pythonic" (for some value of "Pythonic") or just didn't have the exact flavour I wanted. Whatever.

I know that most Pythonistas look down on XML a bit but you really
need to use it to get by in most web projects, especially those involving data formats.
So unless you want to spend hours hand-coding XML you are stuck painstakingly
struggling with SAX and DOM interfaces. This is also highlighted by the
over-abundance of XML processing/parsing/binding/etc. frameworks available for Python.

I opted for the time-honoured tradition of re-inventing the wheel.

### Inspiration ###

I shamelessly spent hours poring over the following projects and ripping out all the
coolest features to create this one:

  * Frederik Lundh's [ElementTree](http://effbot.org/zone/element-index.htm) is what I consider to be the best all-around XML library out there
  * Aaron Swartz's [xmltramp](http://www.aaronsw.com/2002/xmltramp/) is the inspiration for the extreme simplicity of the YAXL interface
  * Philippe Normand's [EaseXML](http://easexml.base-art.net/) is more of a Python/XML mapping library than a pure XML manipulation library
  * Fourthought Inc's [4suite](http://4suite.org) is probably the most complete in terms of standards-compliant support for XML and XML-related technologies (DOM, RDF, XSLT, XInclude, XPointer, XLink, XPath, XUpdate, RELAX NG, and XML/SGML Catalogs)
  * [lxml](http://codespeak.net/lxml/) provides a Pythonic binding for the [libxml2](http://xmlsoft.org/) and [libxslt](http://xmlsoft.org/XSLT) libraries which were written in C for the [Gnome](http://www.gnome.org) project

### Acknowledgements ###

The following people have submitted bug reports or enhancement suggestions:

  * Marc
  * "Crest"
  * Marcus Gna
  * [Damian Cugley](http://www.blogger.com/profile/3448376)
  * Lon Barfield

Thank you all for your contribution!

### References ###

  * Henri Sivonen's paper on [HOWTO Avoid Being Called a Bozo When Producing XML](http://hsivonen.iki.fi/producing-xml/)