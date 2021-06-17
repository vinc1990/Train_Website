from django.shortcuts import render
import json


def homepage():
	tree = [
             {
                 'text': "第一部分:发电工程",
                 'href': 'javascript:;',
				 'state': {
                        'expanded': False,
                    },
                 'nodes': [
                     { 'text': "第一章:热机工程", 'href': "javascript:;rjgc.pdf",},
                     { 'text': "第二章:热机工艺", 'href': "javascript:;rjgy.pdf",},
                     { 'text': "第三章:电气专业", 'href': "javascript:;dqzy.pdf",},
                     { 'text': "第四章:结构专业", 'href': "javascript:;jg.pdf",},
                     { 'text': "第五章:水工工艺", 'href': "javascript:;sggy.pdf",},
                     { 'text': "第六章:水工结构", 'href': "javascript:;sgjg.pdf",},
                     { 'text': "第七章:总图专业", 'href': "javascript:;zt.pdf",},
                     { 'text': "第八章:施工组织", 'href': "javascript:;sgzz.pdf",},
                     { 'text': "第九章:化学专业", 'href': "javascript:;hx.pdf",},
                     { 'text': "第十章:热控专业", 'href': "javascript:;rk.pdf",},

                 ]
             },
            {
                'text': "第二部分:电网工程",
                'href': 'javascript:;',
				'state': {
                        'expanded': False,
                    },
                'nodes': [
                    { 'text': "第一章:变电电气一次", 'href': "javascript:;bddq1.pdf",},
                    { 'text': "第二章:变电电气二次", 'href': "javascript:;bddq2.pdf",},
                    { 'text': "变电电气专题1", 'href': "javascript:;bddqzt1.pdf",},
                    { 'text': "变电电气专题2", 'href': "javascript:;bddqzt2.pdf",},
                    { 'text': "变电电气专题3", 'href': "javascript:;bddqzt3.pdf",},
                    { 'text': "变电电气专题4", 'href': "javascript:;bddqzt4.pdf",},
                    { 'text': "变电电气专题5", 'href': "javascript:;bddqzt5.pdf",},
                    { 'text': "变电电气专题6", 'href': "javascript:;bddqzt6.pdf",},
                    { 'text': "变电电气专题7", 'href': "javascript:;bddqzt7.pdf",},
                    { 'text': "第三章:变电土建", 'href': "javascript:;bdtj.pdf",},
                    { 'text': "变电土建专题1", 'href': "javascript:;bdtjzt1.pdf",},
                    { 'text': "变电土建专题2", 'href': "javascript:;bdtjzt2.pdf",},
                    { 'text': "变电土建专题3", 'href': "javascript:;bdtjzt3.pdf",},
                    { 'text': "第四章:送电电气", 'href': "javascript:;sddq.pdf",},
                    { 'text': "送电电气专题2_设计计算程序", 'href': "javascript:;sddq2.pdf",},
                    { 'text': "送电电气专题3_气象条件选择", 'href': "javascript:;sddq3.pdf",},
                    { 'text': "送电电气专题4、5_导线、地线和OPGW选择", 'href': "javascript:;sddq4-5.pdf",},
                    { 'text': "送电电气专题7_防雷及接地", 'href': "javascript:;sddq7.pdf",},
                    { 'text': "送电电气专题8_杆塔规划", 'href': "javascript:;sddq8.pdf",},
                    { 'text': "送电电气专题9_绝缘子串型及金具研究", 'href': "javascript:;sddq9.pdf",},
                    { 'text': "送电电气专题10_跳线设计", 'href': "javascript:;sddq10.pdf",},
                    { 'text': "送电电气专题11_特种导线及大截面导线应用研究", 'href': "javascript:;sddq11.pdf",},
                    { 'text': "送电电气专题12_国外相关标准介绍及国内外标准对比", 'href': "javascript:;sddq12.pdf",},
                    { 'text': "送电电气专题13_大跨越设计", 'href': "javascript:;sddq13.pdf",},
                    { 'text': "送电电气专题14(1)_交流输电线路通保设计", 'href': "javascript:;sddq14-1.pdf",},
                    { 'text': "送电电气专题14(2)_直流输电线路通保设计", 'href': "javascript:;sddq14-2.pdf",},
                    { 'text': "第五章:送电结构", 'href': "javascript:;sdjg.pdf",},
                    { 'text': "送电结构专题1_架空送电线路杆塔选型及优化设计", 'href': "javascript:;sdjgzt1.pdf",},
                    { 'text': "送电结构专题2_基础部分", 'href': "javascript:;sdjgzt2.pdf",},
                    { 'text': "送电结构专题3_ASCE10-97与国内规范比较", 'href': "javascript:;sdjgzt3.pdf",},
                    { 'text': "送电结构专题4_高强钢在输电线路工程中的应用", 'href': "javascript:;sdjgzt4.pdf",},
                    { 'text': "送电结构专题5_负荷组合", 'href': "javascript:;sdjgzt5.pdf",},
                    { 'text': "送电结构专题6_架空输电线路自立式铁塔试验方案", 'href': "javascript:;sdjgzt6.pdf",},
                    { 'text': "送电结构专题7_地基处理及基础防护", 'href': "javascript:;sdjgzt7.pdf",},
                    { 'text': "送电结构专题8_大跨越杆塔与基础设计", 'href': "javascript:;sdjgzt8.pdf",},
                ]
            },
            {
                'text': "第三部分:新能源工程",
                'href': 'javascript:;',
				'state': {
                        'expanded': False,
                    },
                'nodes': [
                        { 'text': "第一章:电气二次", 'href': "javascript:;xnydq2.pdf",},
                        { 'text': "第二章:电气一次", 'href': "javascript:;xnydq1-feng.pdf",},
                        { 'text': "第三章:总图", 'href': "javascript:;xnyzt.pdf",},
                        { 'text': "第四章:施工组织", 'href': "javascript:;xnysgzz.pdf",},
                ]
            },
          {
              'text': "第四部分:IGCC工程",
              'href': 'javascript:;',
			  'state': {
                        'expanded': False,
                    },
              'nodes': [
                      { 'text': "第一章:工艺专业", 'href': "javascript:;igccgy.pdf",},
                      { 'text': "第二章:设备专业", 'href': "javascript:;igccsb.pdf",},
                      { 'text': "主设人工作手册附录", 'href': "javascript:;igccfl.pdf",},

              ]
          },
         {
             'text': "第五部分:建筑与民用工程",
             'href': 'javascript:;',
			 'state': {
                        'expanded': False,
                    },
             'nodes': [
                     { 'text': "第一章:建筑专业", 'href': "javascript:;jmjz.pdf",},
                     { 'text': "建筑专业附录", 'href': "javascript:;jmjzfl.pdf",},
                     { 'text': "第二章:暖通专业", 'href': "javascript:;jmnt.pdf",},
             ]
         },
         {
             'text': "第六部分:勘测工程",
             'href': 'javascript:;',
			 'state': {
                        'expanded': False,
                    },
             'nodes': [
                 { 'text': "第一章:岩土工程", 'href': "javascript:;kcyt.pdf",},
                 { 'text': "第二章:测绘专业", 'href': "javascript:;kcch.pdf",},
                 { 'text': "第三章:水文气象", 'href': "javascript:;kcswqx.pdf",},
             ]
         },
        {
            'text': "第七部分:系统工程",
            'href': 'javascript:;',
			'state': {
                        'expanded': False,
                    },
            'nodes': [
                { 'text': "第一章:系统规划", 'href': "javascript:;xtgh.pdf",},
                { 'text': "第二章:调度自动化", 'href': "javascript:;xtdd.pdf",},
                { 'text': "第三章:通信专业", 'href': "javascript:;xttx.pdf",},
                { 'text': "第四章:继电保护", 'href': "javascript:;xtjd.pdf",},

            ]
        },
        {
            'text': "第八部分:技术经济",
            'href': 'javascript:;',
			'state': {
                        'expanded': False,
                    },
            'nodes': [
                { 'text': "第一章:技经专业", 'href': "javascript:;jjzy.pdf",},
            ]
        },

        {
            'text': "第九部分:环境工程",
            'href': 'javascript:;',
			'state': {
                        'expanded': False,
                    },
            'nodes': [
                { 'text': "第一章:环评专业", 'href': "javascript:;hjhp.pdf",},
                { 'text': "第二章:水保专业", 'href': "javascript:;hjsb.pdf",},

            ]
        },

        ]
	content = {'tree': json.dumps(tree),
				'pattern_name':'designer',
                'filepath':"'zsr'"
				}
	return content

def index(request):
	content = homepage()
	return render(request, 'index.html', content)

def designer(request):
	content = homepage()
	return render(request, 'index.html', content)

def manager(request):
	tree = [
        {
            'text': "第一部分:项目管理基础知识", 
            'href': 'javascript:;',
			'state': {
                        'expanded': False,
                    },
            'nodes': [
                { 'text': "第一章:项目管理基础知识汇总", 'href': "javascript:;2.pdf",  },
            ]
        },
        {
            'text': "第二部分:专业设计基础知识", 
            'href': 'javascript:;',
			'state': {
                        'expanded': False,
                    },
            'nodes': [
                { 'text': "第一章:电站燃煤锅炉及辅助系统设计基础知识", 'href': "javascript:;21.pdf",  },
                { 'text': "第二章:电站汽轮机及辅助系统设计基础知识", 'href': "javascript:;22.pdf",  },
                { 'text': "第三章:燃气-蒸汽联合循环电厂基础知识", 'href': "javascript:;23.pdf",  },
                { 'text': "第四章:热电(冷)联供基础知识", 'href': "javascript:;24.pdf",  },
                 { 'text': "第五章:电厂接入系统基础知识", 'href': "javascript:;25.pdf",  },
                 { 'text': "第六章:电气一次线专业设计基础知识", 'href': "javascript:;26.pdf",  },
                 { 'text': "第七章:电气二次线专业设计基础知识", 'href': "javascript:;27.pdf",  },
                 { 'text': "第八章:总图专业基础知识", 'href': "javascript:;28.pdf",  },
                 { 'text': "第九章:建筑专业基础知识", 'href': "javascript:;29.pdf",  },
                 { 'text': "第十章:土建结构专业基础知识", 'href': "javascript:;210.pdf",  },
                 { 'text': "第十一章:水工工艺专业基础知识", 'href': "javascript:;211.pdf",  },
                 { 'text': "第十二章:水工结构专业基础知识", 'href': "javascript:;212.pdf",  },
                 { 'text': "第十三章:热控专业设计基础知识", 'href': "javascript:;213.pdf",  },
                 { 'text': "第十四章:输煤专业设计基础知识", 'href': "javascript:;214.pdf",  },
                 { 'text': "第十五章:除灰专业设计基础知识", 'href': "javascript:;215.pdf",  },
                 { 'text': "第十五章:除灰专业设计基础知识-附件101", 'href': "javascript:;215-101.pdf",  },
                    { 'text': "第十五章:除灰专业设计基础知识-附件102", 'href': "javascript:;215-102.pdf",  },
                    { 'text': "第十五章:除灰专业设计基础知识-附件104", 'href': "javascript:;215-104.pdf",  },
                    { 'text': "第十五章:除灰专业设计基础知识-附件105", 'href': "javascript:;215-105.pdf",  },
                    { 'text': "第十五章:除灰专业设计基础知识-附件1C05", 'href': "javascript:;215-1C05.pdf",  },
                    { 'text': "第十六章:电厂化学专业设计基础知识", 'href': "javascript:;216.pdf",  },
                 { 'text': "第十七章:暖通专业设计基础知识", 'href': "javascript:;217.pdf",  },
                 { 'text': "第十八章:大件设备运输基础知识", 'href': "javascript:;218.pdf",  },
                 { 'text': "第十九章:施工组织专业基础知识", 'href': "javascript:;219.pdf",  },
                 { 'text': "第二十章:工程地质、岩土工程基础知识", 'href': "javascript:;220.pdf",  },
                 { 'text': "第二十一章:测绘基础知识", 'href': "javascript:;221.pdf",  },
                 { 'text': "第二十二章:水文地质基础知识", 'href': "javascript:;222.pdf",  },
                 { 'text': "第二十三章:水文气象基础知识", 'href': "javascript:;223.pdf",  },
                 { 'text': "第二十四章:火电厂环境保护基础知识", 'href': "javascript:;224.pdf",  },
                 { 'text': "第二十五章:水土保持专业设计基础知识", 'href': "javascript:;225.pdf",  },
                 { 'text': "第二十六章:劳动安全职业卫生基础知识", 'href': "javascript:;226.pdf",  },
                 { 'text': "第二十七章:脱硫脱硝设计基础知识", 'href': "javascript:;227.pdf",  },
                 { 'text': "第二十八章:火力发电工程造价基础知识", 'href': "javascript:;228.pdf",  },
                 { 'text': "第二十九章:火力发电工程财务评价基础知识", 'href': "javascript:;229.pdf",  },
                 { 'text': "第三十章:秸秆电站基础知识", 'href': "javascript:;230.pdf",  },
                 { 'text': "第三十一章:IGCC基础知识", 'href': "javascript:;231.pdf",  },
                 { 'text': "第三十二章:火力发电燃煤锅炉烟气除尘", 'href': "javascript:;232.pdf",  },

            ]
        },
        {
            'text': "第三部分:综合技术", 
            'href': 'javascript:;',
			'state': {
                        'expanded': False,
                    },
            'nodes': [
					{ 'text': "第一章:厂址选择原则和方案比较", 'href': "javascript:;31.pdf",  },
					{ 'text': "第二章:火力发电厂总布置设计方案优化", 'href': "javascript:;32.pdf",  },
					{ 'text': "第四章:项目规划容量与机组选型", 'href': "javascript:;34.pdf",  },
				     { 'text': "第五章:节能减排技术", 'href': "javascript:;35.pdf",  },
				     { 'text': "第六章:节约用水措施", 'href': "javascript:;36.pdf",  },
				     { 'text': "第七章:电力工程设计招标、投标工作要点", 'href': "javascript:;37.pdf",  },
				     { 'text': "第八章:电力工程设备招标、评标工作要点", 'href': "javascript:;38.pdf",  },
				     { 'text': "第九章:空冷技术", 'href': "javascript:;39.pdf",  },
				     { 'text': "第十章:冷却塔排烟技术", 'href': "javascript:;310.pdf",  },
				     { 'text': "第十一章:海水淡化技术", 'href': "javascript:;311.pdf",  },
            ]
        },
      {
          'text': "第四部分:相关设计技术", 
          'href': 'javascript:;',
		  'state': {
                        'expanded': False,
                    },
          'nodes': [
                  { 'text': "第一章:核电站基础知识", 'href': "javascript:;41.pdf",  },
                  { 'text': "第二章:风力发电基础知识", 'href': "javascript:;42.pdf",  },
                  { 'text': "第三章:太阳能光伏及光热发电", 'href': "javascript:;43.pdf",  },
                   { 'text': "第四章:CO2捕集技术", 'href': "javascript:;44.pdf",  },
          ]
      },
    ]
	content = {'tree': json.dumps(tree),
				'pattern_name':'manager',
                'filepath':"'jlr'"
				}
	return render(request, 'index.html', content)
