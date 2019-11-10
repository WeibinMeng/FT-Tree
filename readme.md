# Paper

Our paper is published on IEEE/ACM International Symposium on Quality of Service. The information can be found here:

* Title: Syslog Processing for Switch Failure Diagnosis and Prediction in Datacenter Networks
* Authors: Shenglin Zhang, Weibin Meng, Jiahao Bu, Sen Yang, Ying Liu, Dan Pei, Jun(Jim) Xu, Yu Chen, Hui Dong, Xianping Qu, Lei Song
* Paper link: [paper](https://netman.aiops.org/wp-content/uploads/2015/12/IWQOS_2017_zsl.pdf)

## 环境： 
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
		* -logs：logs to match
	


