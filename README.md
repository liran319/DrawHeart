笛卡尔的第十三封情书——用matplotlib画一颗真心(红)

这两天教一个盆友python的基础，教着教着她问，程序猿一般怎么表白，会不会突然屏幕哪弹出来一颗大红心，于是乎想着，学习编程，怎么着也不能像大学里学c那么枯燥，得有乐趣呀..

蓝后就想起之前在知乎上看见的一个神奇的事件, 具体的么，喏[http://www.zhihu.com/question/21239607]
PS1: 这里神奇的是题主和答主竟然在一起了！！！！羡煞旁人！！
所以勇敢的去追吧！！骚年！
[strong]具体公式就是：「r=a(1-sin θ)」[/strong], 咳咳，这里是极坐标，当然直角坐标系好写，直观，但是公式是二元二次方程，代码稍微麻烦点，先选简单的粗暴的解决问题先。

扯回正题，查了一下python画图的库，于是就有了numpy和matplotlib.
安装过程中不太顺利，主要是windows下cmd里去用easy_install matplotlib 或者pip install matplotlib 都没办法顺利安装，墙内墙外都不成。
好在直接去官网下了安装包，但是光安装exe或者msi还是不成的，会有很多细节没办法完成。
所以重启电脑，再次easy_install matplotlib ，顺利安装（亲测*2 次，妥妥的）。

接下来就是代码啦，我们去matplotlib的官方网站去看，它有很多现成的模型，我们找一个极坐标的，咦，[http://matplotlib.org/examples/pylab_examples/polar_demo.html]
在这里的示例代码里，theta其实就是我们公式里的θ.

ax = plt.subplot(111, polar=True) 这一行里面刚好有个参数polar就是polar coordinate: 极坐标的意思，polar=True刚好就解决了直角坐标系无法适应上面公式的问题。

ax.plot(theta, r, color='r', linewidth=3) 这里是画线的方法，括号里的参数分别是theta 和r，但是我们的目标不是示例中的螺旋线，所以
ax.plot(theta, 1 - np.sin(theta), color='r', linewidth=2) 这才是我们正确的心形图像。
运行一下，看粗来的是不是想要的！
咦貌似还不错是伐？
咦貌似还不错是伐？


但素要显得实心一点吧，是不是更好看？那这里我们就不能用ax.plot()的方法，而是要用fill(填充)，
再看看结果.