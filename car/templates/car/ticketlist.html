<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" isELIgnored="false"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>

	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>车票列表</title>
		<link rel="stylesheet" type="text/css" href="css/header.css" />
		<link rel="stylesheet" type="text/css" href="css/iconfont.css" />
		<link rel="stylesheet" type="text/css" href="css/command.css" />
		<link rel="stylesheet" type="text/css" href="css/clear.css"/>
		<link rel="stylesheet" type="text/css" href="css/index.css"/>
		<script src="jquery-1.11.3/jquery.min.js" type="text/javascript" charset="utf-8"></script>
		 <style>
            * {margin: 0;padding: 0}
            #calendar {width: 300px;margin: 100px auto;overflow: hidden;border: 1px solid #000;padding: 20px;position: relative;z-index: 999;background: #fff;}
            #calendar h4 {text-align: center;margin-bottom: 10px}
            #calendar .a1 {position: absolute;top: 20px;left: 20px;}
            #calendar .a2 {position: absolute;top: 20px;right: 20px;}
            #calendar .week {height: 30px;line-height: 20px;border-bottom: 1px solid #000;margin-bottom: 10px}
            #calendar .week li {float: left;width: 30px;height: 30px;text-align: center;list-style: none;}
            #calendar .dateList {overflow: hidden;clear: both}
            #calendar .dateList li {float: left;width: 30px;height: 30px;text-align: center;line-height: 30px;list-style: none; cursor:pointer;}
            #calendar .dateList .ccc {color: #ccc;cursor:auto;}
            #calendar .dateList .red {background: #F90;color: #fff;}
            #calendar .dateList .sun {color: #f00;}
            .boxs{
            	display: inline-block;
            	position: relative;
            }
            #top_cities {
    			PADDING-RIGHT: 2px;
    			PADDING-LEFT: 2px;
   				PADDING-BOTTOM: 2px;
    			COLOR: #666666;
   			 	PADDING-TOP: 2px;
    			margin-bottom: 2px;
   				BORDER-BOTTOM: #f0f0f2 1px solid;
   				background: #fff;
			}
            #fromStationShow{
            	position: absolute;
            	top: 25px;
            	left: 64.5px;
            	width: 11em ;
            	z-index: 999;
            }
            #calendar{
           	 	position: absolute;
            	top: 0;
            	left: 0;
            	
            	transform: translateY(-30%);
            }
            #flip_cities{
            	letter-spacing: 0.3em;
            }
        </style>
        <script type="text/javascript">
            $(function() {

                //必要的数据
                //今天的年 月 日 ；本月的总天数；本月第一天是周几？？？
                var iNow=0;
                
                function run(n) {

                    var oDate = new Date(); //定义时间
                    oDate.setMonth(oDate.getMonth()+n);//设置月份
                    var year = oDate.getFullYear(); //年
                    var month = oDate.getMonth(); //月
                    var today = oDate.getDate(); //日

                    //计算本月有多少天
                    var allDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month];

                    //判断闰年
                    if(month == 1) {
                        if(year % 4 == 0 && year % 100 != 0 || year % 400 == 0) {
                            allDay = 29;
                        }
                    }

                    //判断本月第一天是星期几
                    oDate.setDate(1); //时间调整到本月第一天
                    var week = oDate.getDay(); //读取本月第一天是星期几

                    //console.log(week);
                  $(".dateList").empty();//每次清空
                    //插入空白

                    for(var i = 0; i < week; i++) {
                        $(".dateList").append("<li></li>");
                    }

                    //日期插入到dateList
                    for(var i = 1; i <= allDay; i++) {
                        $(".dateList").append("<li>" + i + "</li>")
                    }
                    //标记颜色=====================
                    $(".dateList li").each(function(i, elm){
                        //console.log(index,elm);
                        var val = $(this).text();
                        //console.log(val);
                        if (n==0) {
                            if(val<today){
                            $(this).addClass('ccc')
                        }else if(val==today){
                            $(this).addClass('red')
                        }else if(i%7==0  ||  i%7==6   ){
                            $(this).addClass('sun')
                        }
                        }else if(n<0){
                            $(this).addClass('ccc')
                        }else if(i%7==0  ||  i%7==6   ){
                            $(this).addClass('sun')
                        }
                    });

                    //定义标题日期
                    $("#calendar h4").text(year + "年" + (month + 1) + "月");
                };
                run(0);
                
                $(".a1").click(function(){
                    iNow--;
                    run(iNow);
                });
                
                $(".a2").click(function(){
                    iNow++;
                    run(iNow);
                })
            });
        </script>
	</head>

	<body>
		<!-- 页面加载进度 -->
		<div id="page-loading" class="page-loading"></div>
		<!-- 头部 -->
		<div class="header">
			<div class="header">
				<div class="wrapper">
					<!-- 头部内容 -->
					<div class="header-con">
						<h1 class="logo">
                <a name="g_href" data-type="1" data-href="index.html" data-redirect="Y" href="index.jsp">中国铁路12306</a>
            </h1>
						<div class="header-right">
							<!-- 搜索条 -->
							<div class="header-search">
								<div class="search-bd">
									<input type="password" value="" style="display:none">
									<input type="text" class="search-input" id="search-input" value="" placeholder="搜索车票/餐饮/常旅客/相关规章" auto-complete="new-password">
									<!-- 搜索提示 -->
									<div class="search-down">
										<a href="javascript:;" class="close">关闭</a>
										<ul class="search-down-list"></ul>
									</div>
									<!-- 搜索历史 -->
									<div class="search-history">
										<a href="javascript:;" class="history-clear">清除</a>
										<h3 class="search-history-tit">搜索历史</h3>
										<ul class="search-history-list">

										</ul>
									</div>
								</div>
								<a class="search-btn" href="javascript:;">
									<i class="icon icon-search"></i>
								</a>
							</div>
							<!-- 右侧菜单 -->
							<ul class="header-menu">
								<li class="menu-item menu-nav">
									<a name="g_href" data-type="2" data-href="view/index.html" data-redirect="Y" href="javascript:;" class="menu-nav-hd">我的12306
										<i class="caret"></i>
									</a>
									<ul class="menu-nav-bd">
										<li>
											<a name="g_href" data-type="2" data-href="view/train_order.html" data-redirect="Y" href="OrderConfirm.jsp">火车票订单</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="view/lineUp_order.html" data-redirect="Y" href="javascript:;">候补订单</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="view/personal_travel.html" data-redirect="Y" href="javascript:;">我的行程</a>
										</li>
										<li class="nav-line"></li>
										<li>
											<a name="g_href" data-type="10" data-href="queryMyOrder.html" data-redirect="Y" href="javascript:;">我的餐饮•特产</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="view/my_insurance.html" data-redirect="Y" href="javascript:;">我的保险</a>
										</li>
										<li>
											<a name="g_href" data-type="3" data-href="welcome.html" data-redirect="Y" href="javascript:;">我的会员</a>
										</li>
										<li class="nav-line"></li>
										<li>
											<a name="g_href" data-type="2" data-href="view/information.html" data-redirect="Y" href="javascript:;">查看个人信息</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="view/userSecurity.html" data-redirect="Y" href="javascript:;">账户安全</a>
										</li>
										<li class="nav-line"></li>
										<li>
											<a name="g_href" data-type="2" data-href="view/passengers.html" data-redirect="Y" href="javascript:;">常用联系人</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="view/address_init.html" data-redirect="Y" href="javascript:;">车票快递地址</a>
										</li>
										<li class="nav-line"></li>
										<li>
											<a name="g_href" data-type="2" data-href="view/icentre_serviceQuery.html" data-redirect="Y" href="javascript:;">温馨服务查询</a>
										</li>
									</ul>
								</li>
								<li class="menu-item menu-line">|</li>
								<li id="J-header-login" class="menu-item menu-login">
									<a name="g_href" data-type="2" data-href="resources/login.html" data-redirect="Y" href="login.jsp">登录</a>
									<a name="g_href" data-type="2" data-href="regist/init" data-redirect="Y" href="register.jsp" class="ml">注册</a>
								</li>
								<li id="J-header-logout" style="display: none;" class="menu-item menu-nav menu-login">
									您好，
									<a name="g_href" id="username" data-type="2" data-href="view/index.html" data-redirect="Y" href="javascript:;" class="txt-primary menu-nav-my-hd">${sessionScope.name }</a>&nbsp;|&nbsp;
									<a class="logout" href="javascript:;" id="logout">退出</a>
								</li>
							</ul>
						</div>
					</div>
				</div>
				<!-- 导航 -->
				<div class="nav-box">
					<ul class="nav">
						<li id="J-index" class="nav-item nav-item-w1">
							<a name="g_href" data-type="1" data-href="index.html" data-redirect="Y" href="index.jsp" class="nav-hd">首页</a>
						</li>
						<li id="J-chepiao" class="nav-item nav-item-w1">
							<a href="javascript:void(0)" class="nav-hd">车票
								<i class="icon icon-down"></i>
							</a>
							<div class="nav-bd">
								<div class="nav-bd-item nav-col2">
									<h3 class="nav-tit">购买</h3>
									<ul class="nav-con">
										<li class="nav_dan">
											<a name="g_href" data-type="2" data-href="leftTicket/init?linktypeid=dc" data-redirect="Y" href="ticketlist.jsp">单程</a>
										</li>
										<li class="nav_wang">
											<a name="g_href" data-type="2" data-href="leftTicket/init?linktypeid=wf" data-redirect="Y" href="javascript:;">往返</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="lcQuery/init" data-redirect="Y" href="javascript:;">接续换乘</a>
										</li>
										<li></li>
									</ul>
								</div>
								<div class="nav-bd-item nav-col2">
									<h3 class="nav-tit">变更</h3>
									<ul class="nav-con">
										<li class="nav_ref">
											<a name="g_href" data-type="2" data-href="view/train_order.html?type=2&typefilt=4" data-redirect="Y" href="javascript:;">退票</a>
										</li>
										<li class="nav_res">
											<a name="g_href" data-type="2" data-href="view/train_order.html?type=2&typefilt=2" data-redirect="Y" href="javascript:;">改签</a>
										</li>
										<li class="nav_chg">
											<a name="g_href" data-type="2" data-href="view/train_order.html?type=2&typefilt=3" data-redirect="Y" href="javascript:;">变更到站</a>
										</li>
										<li></li>
									</ul>
								</div>
								<div class="nav-bd-item nav-col2">
									<h3 class="nav-tit border-none">更多</h3>
									<ul class="nav-con">
										<li>
											<a name="g_href" data-type="1" data-href="view/ticket/zt_card.html" data-redirect="Y" href="javascript:;">中铁银通卡</a>
										</li>
										<li class="border-none">
											<a name="g_href" data-type="1" data-href="view/ticket/through_train.html" data-redirect="Y" href="javascript:;">广九直通车</a>
										</li>
										<li>
											<a name="g_href" data-type="1" data-href="view/ticket/railway.html" data-redirect="Y" href="javascript:;">市郊快速铁路</a>
										</li>
										<li>
											<a name="g_href" data-type="1" data-href="view/ticket/international_train.html" data-redirect="Y" href="javascript:;">国际列车</a>
										</li>
									</ul>
								</div>
							</div>
						</li>
						<li id="J-tuangoufuwu" class="nav-item ">
							<a href="javascript:void(0) " class="nav-hd ">团购服务
								<i class="icon icon-down "></i>
							</a>
							<div class="nav-bd ">
								<div class="nav-bd-item nav-col6 ">
									<ul class="nav-con ">
										<li>
											<a name="g_href" data-type="1" data-href="view/group/group_management.html?type=1" data-redirect="Y" href="javascript:;">务工人员</a>
										</li>

										<li>
											<a name="g_href" data-type="1" data-href="view/group/group_management.html?type=2" data-redirect="Y" href="javascript:;">学生团体</a>
										</li>
									</ul>
								</div>
							</div>
						</li>
						<li id="J-huiyuanfuwu" class="nav-item ">
							<a href="javascript:void(0) " class="nav-hd ">会员服务
								<i class="icon icon-down "></i>
							</a>
							<div class="nav-bd ">
								<div class="nav-bd-item nav-col6">
									<ul class="nav-con ">
										<li>
											<a name="g_href" data-type="3" data-href="index.html" data-redirect="Y" href="javascript:;">会员管理</a>
										</li>
										<li>
											<a name="g_href" data-type="3" data-href="index.html" data-redirect="Y" href="javascript:;">积分账户</a>
										</li>
										<li>
											<a name="g_href" data-type="3" data-href="index.html" data-redirect="Y" href="javascript:;">积分兑换</a>
										</li>
										<li>
											<a name="g_href" data-type="3" data-href="index.html" data-redirect="Y" href="javascript:;">会员专享</a>
										</li>
										<li class="border-none ">
											<a name="g_href" data-type="3" data-href="welcome.html" data-redirect="Y" href="javascript:;">会员中心</a>
										</li>
									</ul>
								</div>
							</div>
						</li>
						<li id="J-zhanchefuwu" class="nav-item ">
							<a href="javascript:void(0) " class="nav-hd ">站车服务
								<i class="icon icon-down "></i>
							</a>
							<div class="nav-bd ">
								<div class="nav-bd-item nav-col4 ">
									<ul class="nav-con ">
										<li>
											<a name="g_href" data-type="2" data-href="view/icentre_qxyyInfo.html" data-redirect="Y" href="javascript:;">重点旅客预约</a>
										</li>
										<li>
											<a name="g_href" data-type="1" data-href="view/station/hand.html" data-redirect="Y" href="javascript:;">便民托运</a>
										</li>
										<li>
											<a name="g_href" data-type="1" data-href="view/station/shared_Car.html" data-redirect="Y" href="javascript:;">共享汽车</a>
										</li>
										<li>
											<a name="g_href" data-type="4" data-href="czyd_2143/" data-redirect="Y" href="javascript:;">车站引导</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="view/icentre_lostInfo.html" data-redirect="Y" href="javascript:;">遗失物品查找</a>
										</li>
										<li>
											<a name="g_href" data-type="1" data-href="view/station/train_intro.html" data-redirect="Y" href="javascript:;">动车组介绍</a>
										</li>
										<li>
											<a name="g_href" data-type="1" data-href="view/station/custom_PickUp.html" data-redirect="Y" href="javascript:;">定制接送</a>
										</li>
										<li>
											<a name="g_href" data-type="4" data-href="zcfc_2548/" data-redirect="Y" href="javascript:;">站车风采</a>
										</li>
									</ul>
								</div>
								<!-- <div class="nav-bd-item ">
                        <ul class="nav-con ">
                            <li>
                                <a name="g_href" data-type="4" data-href="czyd_2143/" data-redirect="Y" href="javascript:;">车站引导</a>
                            </li>
                            <li>
                                <a name="g_href" data-type="4" data-href="zcfc_2548/" data-redirect="Y" href="javascript:;">站车风采</a>
                            </li>
                        </ul>
                    </div> -->
							</div>
						</li>
						<li id="J-shanlvfuwu" class="nav-item ">
							<a href="javascript:void(0) " class="nav-hd ">商旅服务
								<i class="icon icon-down "></i>
							</a>
							<div class="nav-bd ">
								<div class="nav-bd-item nav-col6 ">
									<ul class="nav-con ">
										<li>
											<a name="g_href" data-type="10" data-href="index.html" data-redirect="Y" href="javascript:;">餐饮•特产</a>
										</li>
										<li>
											<a name="g_href" data-type="5" data-href="" data-redirect="Y" href="javascript:;">旅游</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="view/my_insurance.html" data-redirect="Y" href="javascript:;">保险</a>
										</li>
									</ul>
								</div>
							</div>
						</li>
						<li id="J-chuxingzhinan" class="nav-item ">
							<a href="javascript:void(0) " class="nav-hd ">出行指南
								<i class="icon icon-down "></i>
							</a>
							<div class="nav-bd ">
								<div class="nav-bd-item nav-col2 ">
									<h3 class="nav-tit ">常见问题</h3>
									<ul class="nav-con ">
										<li>
											<a name="g_href" data-type="2" data-href="gonggao/ticketType.html" data-redirect="Y" href="javascript:;">车票</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="gonggao/ticketWindow.html" data-redirect="Y" href="javascript:;">购票</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="gonggao/windowEndorse.html" data-redirect="Y" href="javascript:;">改签、变更到站</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="gonggao/windowRefund.html" data-redirect="Y" href="javascript:;">退票</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="gonggao/help.html" data-redirect="Y" href="javascript:;" class="txt-lighter">更多>></a>
										</li>
										<li></li>
									</ul>
								</div>
								<div class="nav-bd-item nav-col2 ">
									<h3 class="nav-tit ">旅客须知</h3>
									<ul class="nav-con ">
										<li>
											<a name="g_href" data-type="2" data-href="gonggao/usersNeedToKnow.html?linktypeid=txt" data-redirect="Y" href="javascript:;">铁路电子客票</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="gonggao/saleTicketMeans.html?linktypeid=means5" data-redirect="Y" href="javascript:;">身份核验</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="gonggao/help.html" data-redirect="Y" href="javascript:;" class="txt-lighter">更多>></a>
										</li>
										<li></li>
									</ul>
								</div>
								<div class="nav-bd-item nav-col2 ">
									<h3 class="nav-tit border-none ">相关章程</h3>
									<ul class="nav-con ">
										<li>
											<a name="g_href" data-type="2" data-href="gonggao/saleTicketMeans.html?linktypeid=means1" data-redirect="Y" href="javascript:;">铁路互联网售票暂行办法</a>
										</li>
										<li class="border-none">
											<a name="g_href" data-type="2" data-href="gonggao/saleTicketMeans.html?linktypeid=means2" data-redirect="Y" href="javascript:;">铁路旅客运输规程</a>
										</li>
										<li style="text-overflow:ellipsis;white-space:nowrap;">
											<a name="g_href" data-type="2" data-href="gonggao/saleTicketMeans.html?linktypeid=means6" data-redirect="Y" href="javascript:;">铁路进站乘车禁止和限制携带品公告</a>
										</li>
										<li class="border-none" style="text-overflow:ellipsis;white-space:nowrap;">
											<a name="g_href" data-type="2" data-href="gonggao/saleTicketMeans.html?linktypeid=means7" data-redirect="Y" href="javascript:;">广深港高速铁路跨境旅客运输组织规则</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="gonggao/help.html" data-redirect="Y" href="javascript:;" class="txt-lighter">更多>></a>
										</li>
										<li></li>
									</ul>
								</div>
							</div>
						</li>
						<li id="J-xinxichaxun" class="nav-item last ">
							<a href="javascript:void(0) " class="nav-hd ">信息查询
								<i class="icon icon-down "></i>
							</a>
							<div class="nav-bd ">
								<div class="nav-bd-item nav-col5 ">
									<h3 class="nav-tit border-none ">常用查询</h3>
									<ul class="nav-con ">
										<li>
											<a name="g_href" data-type="2" data-href="zwdch/init" data-redirect="Y" href="javascript:;">正晚点</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="queryTrainInfo/init" data-redirect="Y" href="javascript:;">时刻表</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="leftTicketPrice/initPublicPrice" data-redirect="Y" href="javascript:;">公布票价</a>
										</li>
										<li>
											<a name="g_href" data-type="1" data-href="view/infos/ticket_check.html" data-redirect="Y" href="javascript:;">检票口</a>
										</li>
										<li>
											<a name="g_href" data-type="1" data-href="view/infos/sale_time.html" data-redirect="Y" href="javascript:;">起售时间</a>
										</li>
										<li>
											<a name="g_href" data-href="https://forecast.lytq.com/pc.html" data-redirect="N" data-target="_blank" href="javascript:;">天气</a>
										</li>
										<li>
											<a name="g_href" data-type="1" data-href="view/infos/jiaotong.html" data-redirect="Y" href="javascript:;">交通查询</a>
										</li>
										<li>
											<a name="g_href" data-type="2" data-href="queryAgencySellTicket/init" data-redirect="Y" href="javascript:;">代售点</a>
										</li>
										<li>
											<a name="g_href" data-type="1" data-href="view/infos/service_number.html" data-redirect="Y" href="javascript:;">客服电话</a>
										</li>
										<li></li>
									</ul>
								</div>
								<div class="nav-bd-item ">
									<ul class="nav-con nav-con-pt ">
										<li class="border-none">
											<a id="gLink" href="javascript:void(0)">最新发布</a>
										</li>
										<li class="border-none">
											<a name="g_href" data-type="6" data-href="queryDishonest/init" data-redirect="Y" href="javascript:;">信用信息</a>
										</li>
									</ul>
								</div>
							</div>
						</li>
					</ul>
				</div>
			</div>

		</div>
		<div class="lay-sear lay-sear-yp clearfix" style="text-align: center;">
		<div class="boxs">
			<span>*</span>出发地：<input name="fromStation" id="fromStation" type="hidden" />
			<input name="fromStationText" maxlength="15" placeholder="简码/汉字" id="fromStationText" style="width:100px;" class="input_20txt_gray" type="text" />
			<div id="fromStationShow" style="display: none;">
				<h4 id="top_cities">简码/汉字</h4>
				<div id="panel_cities">
				</div>
				<div id="flip_cities">
					<a href class="cur" onclick="">1</a>
					<a href onclick="">2</a>
					<a href onclick="">3</a>
					<a href onclick="">4</a>
					<a href onclick="">5</a>
					<a href class="pagetxt" onclick="">>></a>
				</div>
			</div>
		</div>
		
		
		
		<span>*</span>目的地：<input name="toStation" id="toStation" type="hidden" />
		<input name="toStationText" maxlength="15" placeholder="简码/汉字" id="toStationText" style="width:100px;" class="input_20txt_gray" type="text" />
		<div class="boxs">
		出发日： <input type="text" value="2016-4-11"
			class="input_20txt_gray" id="train_start_date" maxlength="15">&nbsp;&nbsp;
			
			<div id="calendar" style="display:none">
            <h4>2013年10月</h4>
            <a href="##" class="a1">上月</a>
            <a href="##" class="a2">下月</a>
            <ul class="week">
                <li>日</li>
                <li>一</li>
                <li>二</li>
                <li>三</li>
                <li>四</li>
                <li>五</li>
                <li>六</li>

            </ul>
            <ul class="dateList"></ul>
        </div>
		</div>
		 
		<a shape="rect" class="btn122s" href="javascript:void(0);"
			onclick="searchTrain('ADULT')"><font color="#ffffff">查询</font></a>&nbsp;&nbsp; <a shape="rect"
			class="btn122s" href="javascript:void(0);"
			onclick="searchTrain('0X00')"><font color="#ffffff">查询学生票</font></a>
	</div>
	<div class="sear-sel-bd" id="sear-sel-bd" style="height: 44px;">
		<!--展开式高度设置为272px，合拢时为72px,一行行高为34，可计算下-->
		<div
			style=" width: 100px; height: 18px; line-height: 18px; padding: 2px 0; float: left; text-align: right; font-weight: 700; font-size: 0.9em">车次类型：</div>
		<input type="checkbox" class="div-font"/>GC-高铁/城际 <input type="checkbox" />D-动车 <input
			type="checkbox" />Z-直达 <input type="checkbox" />T-特快 <input
			type="checkbox" />K-快速 <input type="checkbox" />其他 车次：<input
			type="text" style="width: 100px;" />
	</div>
	<div class="t-list  mt10">
		<table width="100%" id="listTable">
			<thead id="thead">
				<tr style="text-align: center;font-size: 0.8em">
					<th>车次</th>
					<th>出发站<br>到达站</th>
					<th>出发时间<br>到达时间</th>
					<th>历时</th>
					<th>商务座</th>
					<th>一等座</th>
					<th>二等座</th>
					<th>高级软卧</th>
					<th>软卧</th>
					<th>动卧</th>
					<th>硬卧</th>
					<th>软座</th>
					<th>硬座</th>
					<th>无座</th>
					<th>其它</th>
					<th>备注</th>
				</tr>
			</thead>
			<tbody id="tbody" style="text-align: center;"></tbody>
		</table>
	</div>

	<!-- 遮罩 -->
	<div class="dhx_modal_cover" style="display: none; text-align: center margin-top: 20dp;">
		<img alt="" src="img/loading.gif" style="margin-top: 240px;">
	</div>
				<script type="text/javascript">
					/* 登录显示昵称  */
					$(function() {
						var name = "${sessionScope.name}";
						if(name === '' || "undefined" == typeof name) {
							$('#J-header-login').show();
							$('#J-header-logout').hide();
						} else {
							$('#J-header-login').hide();
							$('#J-header-logout').show();
						}
					});
					$('#username').click(function(){
						location.href = 'passengers.jsp';
					});
					$('#logout').click(function(){
						location.href = 'Logout';
					});
					/*   显示当前时间    */
					$(function(){
						var time = new Date();
						var month = time.getMonth() + 1;
						var day = time.getDate();
						month = month >= 10 ? month : "0" + month;
						day = day >= 10 ? day : "0" + day;
						console.log(time.getFullYear() + "-" + month + "-" + day);
						$('#train_start_date').val(time.getFullYear() + "-" + month + "-" + day);
					});
				</script>
				<script type="text/javascript">
					$(function(){
						$('#page-loading').hide();
					});
					$('#train_start_date').click(function(){
						$('#calendar').show();
					});
					$('#train_start_date').blur(function(){
						$('#calendar').hide();
					});
				</script>
				<script type="text/javascript">
					/*  搜索列车   */
					function searchTrain(purpose_codes){
						var leftTicketDTO ={
							train_date:$('#train_start_date').val(),
							from_station:$('#fromStationText').val(),
							to_station:$('#toStationText').val(),
							purpose_codes:purpose_codes
						};
						$('#tbody').empty();
						var url = 'queryZ?leftTicketDTO.train_date=' + leftTicketDTO.train_date + '&leftTicketDTO.from_station='+
						leftTicketDTO.from_station + '&leftTicketDTO.to_station=' + leftTicketDTO.to_station 
						+ '&leftTicketDTO.purpose_codes='+leftTicketDTO.purpose_codes
						$.ajax({
							type:"get",
							url:url,
							async:true,
							success:function(data){
								console.log(data);
								console.log(typeof data);
								console.log(data.trim() == '当前暂无列车');
								if(data.trim() == '当前暂无列车'){
									alert('当前暂无列车');
									return;
								}
								var list = eval("(" + data + ")");
								var $tboby = $('#tbody');
								
								for(var i = 0;i < list.length; i++){
									if(list[i] == "|列车运行图调整"){
										continue;
									}
									var ticket = list[i].split("|");
									if(ticket[0] == '暂停发售') continue;
									$tr = $("<tr id='ticket_"+ticket[2]+"'><td><div>"+ticket[3]
									+"</div><span id='"+ticket[2]+"_"+ticket[16]+"_"+ticket[17]+"_"+
									ticket[35]+"_"+leftTicketDTO.train_date+
									"'class='lookup' onclick='showTicketPrice(this)'> <b title='收起票价' class='open'></b></span>"
									+"</td>"+"<td>"+leftTicketDTO.from_station+"  "+leftTicketDTO.to_station +"</td>"
									+"<td>"+ticket[8]+"  "+ticket[9]+"</td>"+"<td>"+
									ticket[10]+"</td>"+"<td>"+(ticket[25] === '' ? ticket[32]===''?'--':ticket[32] : ticket[25])
									+"</td>"+hasTrain(ticket[31])+hasTrain(ticket[30])
									+hasTrain(ticket[21])+hasTrain(ticket[23])+hasTrain(ticket[33])+hasTrain(ticket[28])+hasTrain(ticket[24])
									+hasTrain(ticket[29])+hasTrain(ticket[26])
									+"<td>"+""+"</td>"+isOrder(leftTicketDTO.train_date,ticket)+"</tr>");
									
									$tboby.append($tr);
								}
							}
						});
					}
					
					function isOrder(time,ticket){
						if(ticket[1] != "预订"){
							return "<td>"+ticket[1]+"</td>";
						}
						return "<td><a href='javascript:' class='btn72' onclick='checkG1234(\""+ticket[2]+"\",\""
							+time+"\",\""+ticket[6]+"\",\""+ticket[7]+"\",\""+ticket[35]+"\",\""+ticket[16]+"\",\""
							+ticket[17]+"\")'>"
							+ticket[1]+"</td>"
					}
					function teTrain(data1,data2){
						if(data1 === '' && data2 === ''){
							return '<td>--</td>';
						}else if(data1 != ''){
							return '<td class="seat" seat="'+data1+'">'+data1+'</td>';
						}else{
							return '<td class="seat" seat="'+data2+'">'+data2+'</td>';
						}
					}
					function hasTrain(data){
						if(data === ''){
							return '<td>--</td>';
						}else{
							return '<td class="seat" seat="'+data+'">'+data+'</td>';
						}
					}
					function checkG1234(train_no,dateTime,from_station,to_station,seat_types,from_station_no,to_station_no){
						var obj = $('#ticket_'+train_no).children();
						console.log(obj);
						var thead = $('#thead th');
						console.log(thead);
						var data = "";
						console.log(thead[4].innerHTML);
						for(var i = 0; i < obj.length; i++){
							if(obj[i].getAttribute("class") == "seat"){
//								var temp = {
//									seat:thead[i].innerHTML,
//									num:obj[i].getAttribute("seat")
//								}
								data +=thead[i].innerHTML +":"+obj[i].getAttribute("seat")+";";
								//data.push(temp);
							}
						}
						//data = JSON.stringify(data);
						if("${sessionScope.name}" != ""){
							url = 'order.jsp?datatime='+dateTime+'&train='+obj[0].firstElementChild.innerHTML+'&from_station='+from_station+'&to_station='+to_station+'&train_no='+train_no+'&data=' + data + '';
							console.log(url);
							console.log(obj[0].firstElementChild.innerHTML);
							$.ajax({
								type:"get",
								url:"queryTicketPrice?train_no="+train_no+"&from_station_no="
								+from_station_no+"&to_station_no="+to_station_no
								+"&seat_types="+seat_types+"&train_date="+dateTime,
								async:true,
								success:function(data){
									var price = eval('(' + data +')');
									var msg = converse(price);
									msg = msg.substring(0,msg.length - 1);
									url = url + "&price=" + msg;
									location.href=url;
								}

							});
							
						}else{
							confirm("请先登录！");
						}
						
						//console.log(data);
					}
					function converse(price){
						var msg = "";
						if("undefined" != typeof price.P){
							msg = msg + "商务座:"+price.P + ";";
						}else if("undefined" != typeof price.A9){
							msg = msg + "商务座:"+price.A9 + ";";
						}
						if("undefined" != typeof price.A1){
							msg = msg + "硬座:"+price.A1 + ";";
						}
						if("undefined" != typeof price.A2){
							msg = msg + "软座:"+price.A2 + ";";
						}
						if("undefined" != typeof price.A3){
							msg = msg + "硬卧:"+price.A3 + ";";
						}
						if("undefined" != typeof price.A4){
							msg = msg + "软卧:"+price.A4 + ";";
						}
						if("undefined" != typeof price.A6){
							msg = msg + "高级软卧:"+price.A6 + ";";
						}
						if("undefined" != typeof price.WZ){
							msg = msg + "无座:"+price.WZ + ";";
						}
						if("undefined" != typeof price.O){
							msg = msg + "二等座:"+price.O + ";";
						}
						if("undefined" != typeof price.M){
							msg = msg + "一等座:"+price.M + ";";
						}
						if("undefined" != typeof price.F){
							msg = msg + "动卧:"+price.F + ";";
						}
						return msg;
					}
				</script>
				<!--<script type="text/javascript">
					var result = undefined;
					var count = 0;
				$('#fromStationText').bind('input propertychange',function(){
						$.ajax({
							type:"post",
							url:"queryCC",
							async:true,
							data:{station:$('#fromStationText').val()},
							success:function(data){
								result = eval('(' + data +')');
								$('#fromStationShow').show();
								var i = 0;
								var top = "";
								if(result.length > 0){
									top = "正在检索：";
								}else{
									top = "无法检索：";
								}
								$('#top_cities').html(top+$('#fromStationText').val());
								var div_list = $('#panel_cities');
								div_list.empty();
								for(count = 0; count < result.length; count ++,i++){
									if(i >= 6) break;
									var item = "citem_" + i;
									var cturn = result[count].stationId;
									var temp ="";
									if(i == 0){
										temp = "<div class='citylineover' id='"+item+"' cturn='"+cturn+"' style='background-color: rgb(232,243,255);'>";
									}else{
										temp = "<div class='cityline' id='"+item+"' cturn='"+cturn+"'>";
									}
									temp += "<span class='ralign'>"+result[count].stationName+"</span>";
									temp += "<span style='float:right' class='ralign'>"+result[count].stationCode+"</span></div>";
									div_list.append(temp);
									$('#fromStationShow').show();
									$('#'+item).click(function(){
										sendCount(result[count]);
									});
								}
							}
						});
					});
					$('#fromStationText').blur(function(){
						$('#fromStationShow').hide();
					});
					$('#fromStationText').click(function(){
						$('#fromStationShow').show();
					});
					function sendCount(count){
						console.log(count);
						$('#fromStationText').val(count.stationName);
					}
				</script>-->
				<script type="text/javascript">
					function showTicketPrice(obj){
						console.log(obj);
						console.log(obj.getAttribute("id"));
						var id = obj.getAttribute("id");
						var data = id.split("_");
						var train_no = data[0];
						var from_station_no = data[1];
						var to_station_no = data[2];
						var seat_types = data[3];
						var train_date = data[4];
						$.ajax({
							type:"get",
							url:"queryTicketPrice?train_no="+train_no+"&from_station_no="
							+from_station_no+"&to_station_no="+to_station_no
							+"&seat_types="+seat_types+"&train_date="+train_date,
							async:true,
							success:function(data){
								var result = eval('(' + data + ')');
								console.log(result);
								obj.setAttribute('onclick','hideTicketPrice(this,"'+train_no+'")');
								var $tr = "<tr tataran="+train_no+"><td colspan=4></td>"+createTd(result.A9)
									+createTd(result.M)+createTd(result.O)+createTd(result.A6)+createTd(result.A4)
									+createTd(result.F)+createTd(result.A3)+createTd(result.A2)+createTd(result.A1)+createTd(result.WZ)
									+"<td></td><td></td></tr>";
								var id = 'ticket_' + train_no;
								$('#'+id).after($tr);
							}
						});
					}
					function createForA9P(msg){
						if(("undefined" == msg.A9 || "undefined" == typeof(msg.A9) || msg.A9 === '') &&
						("undefined" == msg.P || "undefined" == typeof(msg.P) || msg.P === '') ){
							return "<td width='46' algin='center'></td>";
						}else if("undefined" != msg.A9 || "undefined" != typeof(msg.A9) || msg.A9 != ''){
							return "<td width='46' algin='center' class='p-num'>" + msg.A9 + "</td>";
						}
						else if("undefined" != msg.P || "undefined" != typeof(msg.P) || msg.P != ''){
							return "<td width='46' algin='center' class='p-num'>" + msg.P + "</td>";
						}
					}
					function createTd(msg){
						console.log("undefined" == msg || "undefined" == typeof(msg) || msg === '');
						if("undefined" == msg || "undefined" == typeof(msg) || msg === ''){
									return "<td width='46' algin='center'></td>";
								}else{
									return "<td width='46' algin='center' class='p-num'>" + msg + "</td>";
								}
					}
					function hideTicketPrice(obj,data){
						var tr = $('tr[tataran='+data+']');
						console.log("tr:" + tr);
						tr.remove();
						obj.setAttribute('onclick','showTicketPrice(this)');
					}
				</script>
	</body>

</html>