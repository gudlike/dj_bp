Django startbootstrap boilerplate
===============================================

介绍
-----------

使用django和startbootstrap做一个数据分析的项目，包含三个app

- 可视化部分，简单表格使用startbootstrap绘制，复杂图形使用matplotlib
- 集群管理部分，使用kubernetes+saltstack部署和管理Spark+Tensorflow集群
- 爬虫部分，收集数据


截屏
-----------

.. image:: https://github.com/gudlike/dj_bp/blob/master/screenshots/matplotlib.jpg
    :target: https://github.com/gudlike/dj_bp/tree/master/screenshots
    :alt: See Screenshots

`More screenshots <https://github.com/gudlike/dj_bp/tree/master/screenshots>`_

安装指南
-------

from pypi (recommended) ::

    $ pip install django
    $ pip install tensorflow
    $ pip install matplotlib


TODO
----

- 完善可视化部分bug
- 补充集群管理和爬虫部分代码
