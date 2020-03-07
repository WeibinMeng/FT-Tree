# Paper

Our paper is published on IEEE/ACM International Symposium on Quality of Service ([IWQoS 2017](http://iwqos2017.ieee-iwqos.org/),) and [IEEE Access 2020](http://ieeeaccess.ieee.org/). The information can be found here:

* **Syslog Processing for Switch Failure Diagnosis and Prediction in Datacenter Networks**
  Shenglin Zhang, Weibin Meng, Jiahao Bu, Sen Yang, Ying Liu, Dan Pei, Jun(Jim) Xu, Yu Chen, Hui Dong, Xianping Qu, Lei Song. Vilanova i la Geltrú, Barcelona, Spain, 14-16 June 2017.[paper link](https://netman.aiops.org/wp-content/uploads/2015/12/IWQOS_2017_zsl.pdf)
* **Efficient and Robust Syslog Parsing for Network Devices in Datacenter Networks**
  Shenglin Zhang, Ying Liu, Weibin Meng, Jiahao Bu, Sen Yang, Yongqian sun, Dan Pei, Jun Xu, Yuzhi Zhang, Lei Sone, Ming Zhang. [paper link](https://netman.aiops.org/wp-content/uploads/2020/02/FT-tree-IEEE-Access20.pdf)

## Environment： 
	python3, pygraphviz (if draw tree)

## Train：
* python main\_train.py -train\_log\_path training.log -out\_seq_path output.seq  -templates output.template
	* Parameters：
		* -train\_log\_path： rawlog path
		* -out\_seq_path：template index file
		* -templates：template file


## Match：
* python main_match.py -templates ./output.template -logs training.log
	* Parameters：
		* -templates： template path
		* -logs：logs which need to match
	


