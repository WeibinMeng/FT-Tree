# Paper

Our paper is published on IEEE/ACM International Symposium on Quality of Service. The information can be found here:

* Title: Syslog Processing for Switch Failure Diagnosis and Prediction in Datacenter Networks
* Authors: Shenglin Zhang, Weibin Meng, Jiahao Bu, Sen Yang, Ying Liu, Dan Pei, Jun(Jim) Xu, Yu Chen, Hui Dong, Xianping Qu, Lei Song
* Paper link: [paper](https://netman.aiops.org/wp-content/uploads/2015/12/IWQOS_2017_zsl.pdf)

## 环境：
	python3, pygraphviz
	
## 训练&匹配日志整合：
* 运行命令：python main\_train.py -train\_log\_path training.log -out\_seq_path output.seq  -templates output.template
	* 参数解释：
		* -train\_log\_path： 训练所需要的原始日志
		* -out\_seq_path：日志匹配完之后的编号序列
		* -templates：输出的模板文件
	* **注意：使用该算法时，最好将数据集中前面几列时间、消息类型的信息删掉，要不然比较乱**。


## 每个文件的作用
### 训练日志模板：
* 输出文件：模板、单词词频列表
	* 运行脚本的的命令：
		* python ft\_tree.py -FIRST\_COL 0 -NO\_CUTTING 1 -CUTTING\_PERCENT 0.3 -data\_path ./training.log -template_path ./output.template -fre\_word\_path ./output.fre -picture\_path ./tree.png -leaf\_num 4 -short\_threshold 5 -plot\_flag 1
	* 参数样例：
	   * FIRST\_COL 每行日志从第几列作为输入，默认为0
	   * NO\_CUTTING = 0 #初步设定1时，是前30% 不剪枝 ,全局开关， 当其为0时，全局按照min_threshold剪枝
	   * CUTTING\_PERCENT =0.6 #前百分之多少是不剪枝的 
		* train\_log\_path='input.txt'
	   *   template\_path = "./logTemplate.txt" #模板
	    *   fre\_word\_path = "./fre_word.txt"   #
	    *   leaf\_num = 4 #剪枝数
	    *    picture\_path = './tree.png'
	    *  short\_threshold = 2 #过滤掉长度小于5的日志
	    *  plot\_flag 默认为0，不画图，若为1，则将ft\_tree画出来，会同时画出“短模板”（蓝色）和“剪枝结点”(红色)

	
### 匹配ft-tree的日志模板:
* 运行脚本的的命令：
	* python3 matchTemplate.py -short\_threshold 5 -leaf\_num 6 -template\_path ./output.template -fre\_word_path ./output.fre -log\_path ./training.log -out\_seq\_path ./output.seq -plot\_flag 0 -CUTTING\_PERCENT 0.3 -NO\_CUTTING 1 **-match\_model 1**
		
* 参数样例：
	*	short\_threshold = 2 #过滤掉长度小于5的日志
	*  leaf\_num 增量学习时的剪枝阈值。(如果将6改成10，可以通过样例数据看出不同匹配机制中的不同效果，即LearnTemplateByIntervals会对新来的数据做剪枝)
	*  template\_path = './output.template'
	*  fre\_word\_path = './output.fre'
	*  runtime\_log\_path = './new.log'
	*  out\_seq\_path = './output.seq'
	*  plot\_flag 0为不画图，1为画图，默认为0。（如树太大不要画图，会卡死）
	*  CUTTING\_PERCENT 指定每条日志的前百分之几的单词不剪枝，增量学习时会用到，正常匹配用不到
	*  NO\_CUTTING 是否每条日志的前几个单词不剪枝，0为正常剪枝，1为不剪枝，默认为1。增量学习时会用到，正常匹配用不到
	*  match\_model 1:正常匹配日志  2:单条增量学习&匹配 3:批量增量学习&匹配
* 增量学习模板：
	* matchLogsAndLearnTemplateOneByOne()函数  单条匹配，如果匹配不到，则学习新的模板。会将新学到的模板插入到模板文件的最后。
	* matchLogsFromFile() 函数，正常匹配日志，如果匹配不到，则为模板序号为0
	* LearnTemplateByIntervals(）函数， 将一时段的日志作为输入，基于以前的模板增量学习，新添加的日志模板也会按照设定的阈值剪枝，最终将新学到的模板插入到模板文件的最后。
			例如在样例数据中，假设新来的日志为newlogs.dat， 原始的模板树为Trace\_train.png,当剪枝k=6时（如图reBuildTree\_k6），会剪枝，当阈值为10时（如图reBuildTree\_k10），会保留一些变量


### 日志模板按照原始日志单词顺序排序:
将模板中的单词按照原日志中的单词顺序排列,得到**正序模板**

* 运行脚本的的命令：
	*  python3 orderWords.py -templates ./output.template -sequences ./output.seq -rawlog ./training.log -order\_templates ./output.template\_order

### 按照正序模板匹配日志:
按照日志原先的单词顺序匹配

* 运行脚本的的命令：
	* python3 matchTemplate.py -short\_threshold 5 -leaf\_num 6 -template\_path ./output.template\_order -log\_path ./training.log -out\_seq\_path ./output2.seq -plot\_flag 1 -CUTTING\_PERCENT 0.3 -NO\_CUTTING 1 **-match\_model 4**
	
### splitTimeWindows.py:
 模板分析：切分时间窗口，然后统计正常时段、异常时段、全部时段中出现top10的模板，并且画图


### countFreTemplates.py:
 模板分析：输出前10个常出现的模板，以及每个模板对应的日志
 
 
