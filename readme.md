## ft-tree.py：
* 输出文件：模板、单词词频列表
	这个版本的文件中的参数：
   * NO_CUTTING = 0 #初步设定1时，是前60% 不剪枝 ,全局开关， 当其为0时，全局按照min_threshold剪枝
   * CUTTING_PERCENT =0.6 #前百分之多少是不剪枝的 
	* data_path='input.txt'
   *   template_path = "./logTemplate.txt" #模板
    *   fre_word_path = "./fre_word.txt"   #
    *   leaf_num = 4 #剪枝数
    *    picture_path = './tree.png'
    *  short_threshold = 2 #过滤掉长度小于5的日志
	* 画图在"self.drawTree()" ，只有在构建fttree的步骤即本文件中才能同时画出“短模板”（蓝色）和“剪枝结点”(红色)


## matchTemplate.py:
 * 参数：
	*	short_threshold = 2 #过滤掉长度小于5的日志
	*   template_path = './logTemplate.txt'
	*  fre_word_path = './fre_word.txt'
	*  raw_log_path = '../env-itsm-was-systemerr0603.log'
	*   out_seq_path = './test_seq.txt'
* 增量学习模板：
	* matchLogsAndLearnTemplateOneByOne()函数  单条匹配，如果匹配不到，则学习新的模板。会将新学到的模板插入到模板文件的最后。
	* LearnTemplateByIntervals(）函数， 将一时段的日志作为输入，基于以前的模板增量学习，新添加的日志模板也会按照设定的阈值剪枝，最终将新学到的模板插入到模板文件的最后。
			例如在样例数据中，假设新来的日志为newlogs.dat， 原始的模板树为Trace_train.png,当剪枝k=6时（如图reBuildTree_k6），会剪枝，当阈值为10时（如图reBuildTree_k10），会保留一些变量
* 画图： ft_tree.py跟matchTemplate.py 中的 drawTree()函数。

## orderWords.py:
将模板中的单词按照原日志中的单词顺序排列
	
## splitTimeWindows.py:
 模板分析：切分时间窗口，然后统计正常时段、异常时段、全部时段中出现top10的模板，并且画图


## countFreTemplates.py:
 模板分析：输出前10个常出现的模板，以及每个模板对应的日志
 
 
#Paper

Our paper is published on IEEE/ACM International Symposium on Quality of Service. The information can be found here:

* Title: Syslog Processing for Switch Failure Diagnosis and Prediction in Datacenter Networks
* Authors: Shenglin Zhang, Weibin Meng, Jiahao Bu, Sen Yang, Ying Liu, Dan Pei, Jun(Jim) Xu, Yu Chen, Hui Dong, Xianping Qu, Lei Song
* Paper link: [paper](https://netman.aiops.org/wp-content/uploads/2015/12/IWQOS_2017_zsl.pdf)