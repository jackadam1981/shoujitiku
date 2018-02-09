# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-02-04 10:49
# @Author  : Jackadam
# @Email   :
# @File    : read_question.py
# @Software: PyCharm
import requests, json, sqlite3, time, random
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///Plan.db', encoding='utf-8')

Base = declarative_base()  # 生成orm基类


class Question(Base):
    __tablename__ = 'Question'  # 表名
    id = Column(Integer, primary_key=True)
    Question_type = Column(String(32))
    Question = Column(String(128))
    Answer = Column(String(32))
    AnswerA = Column(String(32))
    AnswerB = Column(String(32))
    AnswerC = Column(String(32))
    AnswerD = Column(String(32))
    AnswerE = Column(String(32))
    AnswerF = Column(String(32))


Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

# 基础结束,这以上的放一个文件，引用Session 和数据库结构类
url = 'http://www.shoujitiku.net/YT_WeiXin/GetSt?th='
list = 'ec09c3eb-96d1-40b5-9018-100cac0f4189,d4a6f483-5f61-4ba0-9cf1-d49960772455,0dd43583-aadc-4cfb-ad0b-777c4da7b611,b90b2394-56b7-4fea-bcb7-87b3b4af0a74,bde136c3-dedb-41d4-8f46-ddfb8b3eb5de,7d753ff8-bd89-4bf2-976d-74f956b3e573,64733cc8-5e6a-418a-a800-d2ce0692c261,bf8a7849-007a-43c4-a840-4c8b6bbaf6e0,9a135723-b5df-4c85-a267-02c78a454402,4cd45285-5bc8-4cd4-bc8c-f6b8f4a248d7,2d986839-527b-490f-bd84-1f94c444bf2f,905bf78d-5a12-4195-a089-94f7b8cc4d2d,3a6a8ed8-c5cd-4165-98cf-265b2783ef90,8e1a8b85-8aea-4286-a035-7347bad138f5,e33b9479-163f-456d-9e96-2f0c178901f9,f8b2ecf6-f712-47f2-9a7d-84d37f350a37,4ad590bf-4ba0-4d53-8261-79282907f990,030e5601-b85e-4318-ad51-0988068b3a86,56d162e7-06e3-4fb7-864f-0f0a6f95ff14,d3146f95-b1ba-495b-9079-6c9844b345d2,96b323be-5a5c-4087-9bac-6aac29cd08f1,5fbdc0e7-a65e-4a05-b44d-6f53a1a059d3,4b7f3edb-3a56-41df-a298-7d52935594fb,50f360d4-bed1-41b2-9c47-fea060e31455,5d2b3f94-c337-4160-8de5-2d47d01c7dae,947b9a14-6117-4cb5-8b12-70dee86004ef,233ecd2a-f8ce-4c8c-98f7-81a69578eb35,5dbe5521-2c08-4fe5-9880-8bb5adf03525,b91b2b5b-73b6-478d-a4ce-9748349a5435,4fb05fbd-7bbe-473a-9a77-f44848e1998c,47da502a-99bc-4021-ac7c-1d522be48bc4,3772dcbf-c55c-4dc5-b316-660114326c68,b4cc5471-07b8-4daa-b666-bc5672414f62,29f87a8d-2fbb-4e43-b299-0087813b5ee5,d8d7b214-2c1e-4baa-bc05-35863af44446,23144215-6fbd-48ba-9283-522b94b11c1d,2d6d3214-1812-4a3e-a43f-d65eaac37255,8932f9ca-6416-4dc4-a4bc-35b5bec106f5,72390f66-b0a9-4106-bd40-b93907610809,b021777c-3c96-4524-859a-165de4956c02,322315fd-086b-4b65-b7e7-ab307fe4cb95,1f1f0a4f-0e4f-4417-a3a8-50d2c0d4787b,209d033d-eb91-4cf6-bf53-c490ca54cf57,42b1007f-b899-4960-b121-c4e100f8ef6d,ae6e458b-39ee-4c87-b84e-df61205ff0ac,14117113-08f5-48eb-b9cb-f9d8957a388a,e67cf41d-37ae-423a-9ca0-0d48e2ab534a,01340716-be30-47cc-9e66-6854b796d4f3,dd0c17d3-3888-4d08-beb9-69bae624559b,30b99d7e-8ab6-444a-b85c-7ef864632703,e6841b35-707d-4c36-8eb6-ec0fa08753ba,cfc78bab-48bd-4a69-90de-62710eb1f0da,cda37a99-6ffc-43a9-8189-e526bedecbd9,47ad83c4-3849-4a32-a1ca-31d86143447f,4d192c9e-4e71-4e1b-908d-1a802d5bd257,02ffab1d-5647-44d2-8f05-8309c19ee6f3,c0743dda-ceed-427b-b104-1d8377142ab8,336efe7d-29b9-4eb6-a9d9-098a1564c9f7,b08d4ecd-f0c7-4884-a19e-ce017d342d2e,2d63fbba-0021-493b-9c0f-011c2ab1b96f,331b6628-8508-433c-825c-026c3be67447,486dbfa4-157e-48a6-b955-f90f9ee2a985,df7bd7d3-eabd-472a-9a75-076ae50301ef,8d51a25c-9ea1-44b0-87d5-cc762505948c,78b4953f-d123-4978-9ebe-92c3db4b9dfb,20e53963-a0e1-4a1d-9a3b-4146f9613ec4,e185ef6d-369a-4fe2-a51e-2717553a78b4,2824e2bc-4c69-418a-8249-72e685fede83,4e906876-0842-4d67-bb69-df521a563b31,0c9cd80f-021a-4289-b50e-ef4d564a9e67,57603bb6-8b71-42be-80a7-0155706bee3f,4074a67d-2c63-41a6-bcab-1da1d5cc523a,ed8ad032-057b-4f18-8894-b812c81cc1fb,a0935c18-958b-49da-b634-7fef14cdfba4,c4111e42-88be-4c2b-b894-8561789f7a9b,71b2739d-42d8-4ea5-b921-55ff8eb83d8d,297ecf76-0790-493f-acd6-50d0887abb8c,460aced9-5866-4d29-80bd-d3b34cd51265,c5a07d18-c5be-46ce-8cdc-7d96a0ddceb1,d8e850c3-3852-4c44-90b9-23aa67bc41eb,ddff27b0-07ce-4c08-aa62-e9afcb0013db,9c722957-9988-458b-8dc8-4c03971715db,e7f84536-95b5-4e14-94df-7445af5260ff,f83db8f6-7fdb-4468-b318-b32edbcf7ec3,41300a02-ef08-4fe8-b1ad-882d8d0c519d,c4a3c6fb-3add-41f4-828d-6b9130db0630,c6c080a2-4848-4808-b779-6606a117a9a0,4d467bb3-59e3-41e3-880c-0150a8902262,16c54b91-7519-45dc-b1d5-a026148506bc,45f9d911-a420-4d41-941a-e4a4e2cd231a,859d7b56-e57b-4f93-a9c8-51d03af8a365,9d5a598c-34a9-4d76-a59e-f44ea3ed81ad,545f91f6-6241-4b0a-b369-a0958391d7a6,5999a767-f22b-49d5-8da5-46815be295c2,4fb185d9-0156-4c4f-8ed8-b99e6444496a,ad1504a9-1d5b-4216-8b44-fa656721db1c,8da04432-e290-4d2b-b5c6-0ae2677bb58e,0ee076f1-ba3d-4ded-abaf-62e4a8cd0490,5469ebdc-3066-49b5-9afb-ea293312225a,24f55dbe-207c-4222-85fa-8f77e540be9c,bda391f1-c53e-45e6-b87b-89a3c8d206cb,8e50a8bd-42b1-4439-abb0-acd6255c1267,48bd5ac9-c764-4eb9-b67f-81ac1d809c38,3456eb45-f390-4a93-bcf5-f6ca4ff04a73,a981dc47-c2b7-46ab-bfd8-210d65bd5fd9,84c00bcc-6b17-40dd-a13a-bc8c6a2252ba,b1049ae6-d531-4b6c-82d4-adf0d6c88131,fa19f595-3f04-45ec-a2b4-a4ee3997cc97,28f635d3-5b3a-40c0-8e1f-c54e664337a0,44280719-9414-4a7d-a79e-ecacaa9b7a80,ecc1f255-c621-473e-be67-d0a3aff1f8ec,058af52f-d931-4947-a102-033addda0e28,e60e7a8c-121a-4b3c-b5a8-7d805c996783,e7189972-a97b-4813-ad5a-032515561fde,c35cdb06-fa35-439b-b2e4-147bfcfc1bed,bc315979-9ed2-4db1-a819-80bf99840ccb,75a2ab91-e6ce-43c3-a401-3ac88a03590f,39e362d9-1683-4922-944f-916b976dffbb,dc1f7ea8-5056-4755-9c0a-f73cc3eda9cc,9041e082-c039-4462-91fd-f6b11ce0aa5f,4e5ebec7-fd8c-4cd3-bd10-6a8826482dde,b502d8e0-3d7b-4c24-b4e9-f3dd232a75e7,4c18af98-2fdd-468a-b441-08f1b7f8bfe1,19f0c837-1ae6-4b5e-95fc-cad7dc39c5f8,6cd94ea5-ef27-4365-8169-127825d8f1d5,79ddccc9-0071-46af-8966-cc753358fefb,296fd866-ce08-40ea-a075-cbc18119d4ee,2d30a79a-3a83-4541-a1c5-603fafe2c62e,64017a42-bd5c-46ac-b8a5-f6b0db5a2a88,6570a413-cf1e-4e5a-bfb5-a2cc932c195a,3f1f41c0-8a40-4c9c-b4a0-1c21173cd5b0,2ba99be3-61d1-4cc8-99e3-0ca6051114ba,ffc1c72e-e78c-4cfe-8bcf-475fa6ad663a,4cf874ba-2af5-41e4-a673-c9603652b3b7,1613863e-2045-4d69-90ea-17eb0a25b517,fbc1d5e0-3b8c-419c-9c31-349c8f7db8c4,c37155ff-19bf-4126-a56c-d51862cdb8f2,322e7c08-5458-4413-a9b0-e22bfec16d52,1a94132d-0206-4795-a0b1-067a984b91d4,2abe3691-5e6d-47eb-ad7f-840285f10473,3d071f42-13f4-44f0-a894-ada220abe0f3,55f13368-f2a6-4154-991b-d8748bd8888c,e5890ae6-a4ee-4c24-8649-3161e3bd9987,50ef4cd4-eadb-4c93-a88d-868fa67af0d7,b6fef07a-e90a-426c-ab4c-ac86289c9fcc,742c9287-f97c-437c-a18c-80b0cb6522ee,030a55ed-980a-41a4-9d99-ad02186358f7,a3c20ca7-fa46-4304-a67e-876fbf003b2b,0871c4ff-bd92-4ff2-969c-77cd8d78e47c,848b6f17-7b7a-43e5-94cf-d8582463d3e9,67ddc639-ec8c-48ee-b078-4a7733a170f8,ff9513a9-4b71-4b24-953d-56a8c1b23aa7,b263c9f7-8598-4064-a34a-047ba4404de8,6c8773aa-0cee-4629-874c-1ad0a66375cf,bc2e03ec-5778-41ca-b1be-0ff88dd8c9ff,4c999b32-3b9b-4e33-88b4-7894d9a9c413,77bd8581-03d5-4061-89a2-dea1361fd121,6a2a0dd3-162d-4652-af47-1a0b2fe17ddc,2c7238da-45fb-4d54-8be2-cb9149993e03,754c7015-dbe2-4de1-810e-5f9178023875,42bcb1b2-c949-4926-b8a6-d00668848291,68c42507-7a97-49f5-bf49-dd2bd30f8450,c7801fc7-d929-4221-a90f-8eaf1d56d622,ee08a881-afd0-45ad-8360-d2b80aded30c,57567542-6cdd-458b-87c4-f2664ada1f78,e5be142e-acc5-4c1c-8d16-40c0ff3163b7,fc0436cb-9c96-4f38-8ec8-65f32339f93a,ef31478b-bd40-4373-8b68-03baa1fd4e3d,32820e4b-0282-4513-9f3d-21647bb01a2a,fa9b3f93-47a3-4e3f-9844-dc0de1fec2ea'
list = list.split(',')
for i in list:
    print(i)
    html_json = requests.get(url + i)
    html_dict = json.loads(html_json.text[1:-1])
    html_ip = requests.get('http://httpbin.org/ip')
    print(html_ip.text)

    # 插入开始
    Q_obj = Question(
        Question_type=html_dict.get('Item1'),
        Question=html_dict.get('Item2'),
        Answer=html_dict.get('Item3'),
        AnswerA=html_dict.get('Item4'),
        AnswerB=html_dict.get('Item5'),
        AnswerC=html_dict.get('Item6'),
        AnswerD=html_dict.get('Item7'),
        AnswerE=html_dict.get('Item8'),
        AnswerF=html_dict.get('Item9'),
    )  # 生成你要创建的数据对象
    Session.add(Q_obj)
    Session.commit()  # 现此才统一提交，创建数据
    time.sleep(random.randint(2, 5))