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
list = '9735bd3a-e463-4408-afd8-449d2424cda7,2915c53b-48ec-4f03-b12b-02462be0d9e2,e16c21ee-f4ae-4fbc-a689-1c4fe201affd,6b4b805a-6b69-4ddd-b969-8910de252100,24384415-e28b-486f-92d4-a5a8f6359cbe,e04f2a7a-b060-426e-8a9c-ec78488a513f,e4dd2645-cfd0-4f85-a3c8-724fd74f3eaa,eb394429-4b6e-4ebc-9e4f-36fc87836204,a2d3fc57-f05e-4b5c-8b3a-92ba8016db79,1ab1d127-cde1-4ef0-a992-3732615ba0c0,f5843d7d-2883-4f5b-ad3c-3d044d0a3e42,c41da8bc-e91f-4d81-af16-db1909b9b35f,1d4b3b4b-d854-4de9-a013-9ab0f152a800,4bf48274-1d18-464d-b372-087817e4bc2f,af399812-fec8-4bba-aa0f-645459ab0ea2,cb09334e-fcf8-4433-8fc3-aa8df0f0f002,ce2734d2-9a44-4ccd-9a47-1284691c38f2,8d94f8f0-4fb1-4c0f-9a2f-df922fa29fc8,a60f8f04-5515-4a71-a558-68c80028a605,d72b7ad2-d4ac-46d3-8f70-07c0f089d4b2,5c70b736-1a2d-4aa2-999a-d5b0b9a9d397,e4961440-e235-469b-bd2b-5e8d2e041825,02a0674f-7e53-4186-b798-100496121d01,a887c144-ef5d-4f5b-9e7c-a59fe043417f,a13d1b1e-78a1-41f4-b6ce-c2c016bda21a,1496ac6c-cde0-49b9-9ebf-b692d6e5d915,581eaa72-25d0-4703-a6ee-b8724ac5b8a3,931af07f-14ca-46bd-b31f-a7e8b34419b3,653e96dc-abd1-4c32-a8de-abb6b6cd2284,50a2a573-59a5-43d1-a5c2-5e34ca760cd3,b8dc6594-4b3a-4192-95a5-82de34b22630,1c8cd068-ef43-454f-b4b9-768169574ca4,1ff90e18-4df5-428f-8cb6-36c1c230ca82,8d16683c-b300-4821-a7ac-b8f934cb8090,aadd11eb-04df-408e-a163-aa20b03cfd76,b024a2ed-92e2-4af6-8ad4-e538d45959e6,8affb9a6-0224-463f-90af-3c21f4f97165,e98ecb78-bb06-40e3-86ce-5d70909045c8,06679324-2984-40e2-aa80-61d17a10f0d7,333e8e6b-8c03-4d2e-bfea-dc9119d4795c,64e464d6-1ef4-4355-af16-3fbc88a58205,f37c3f2d-c5fc-45ab-acbc-8b11a1a296e4,bd8d90a6-60da-4bdd-9e99-c3f78ec7a637,4791f65c-38b9-4323-9007-1cfe121ee999,9c5c9864-8fdf-4a7e-87d2-e9bcf9f70b7e,f2080ea7-4a38-439b-b359-1d836aa07500,13cfd7a0-7e27-4a72-b0fd-f56ab90d66eb,6e00fbd9-aec9-45d9-b6ae-0c77a1dc0cc4,048b1a8d-298d-4926-865c-73f3838066bd,04b10722-0b1d-4329-ac0a-e68e03b6145d,1d8feb11-3116-45c3-8c91-b689429afad0,0fd51bb5-d71d-4d14-a327-6c604c34a9c0,1e25a12c-876b-48f6-bf9b-0b00b7b6e68d,bc1f7490-0105-47cf-8af6-b1a7dd54b930,a1c49a2f-202c-4ccf-a58e-7417dd295018,257df478-c93a-45e2-b1b0-f93e4d70d77e,5514295b-48c9-408f-b680-af00d2c9c7a8,6155722b-0a1d-4cd4-9213-9e76b967870d,ec2237b2-46a8-42ed-ab4a-2cfae5480ee4,5e20b7dd-87fe-4f35-92ca-13a37055470f,16991de5-da80-4ec1-99e4-bdd377eaddcd,ff15833c-cc78-4f86-a175-af2fa11b93aa,63ae68eb-2458-4a53-b37a-aea896b89b4e,98b59879-bda5-42d1-89df-85e12257d45c,20af6176-89e0-4695-87f1-84eeaaa2f22d,a9f395e3-60d8-4032-8722-2659bc8dd0c2,5bb6f75d-2105-4af1-948d-32f472011dff,1dbef50b-f2f4-4b86-89a8-acae8e331ef8,b29d18f1-f144-4ae7-a6f5-41684d371b7d,3adc26cb-d233-477a-9cea-23d1f8765b22,f7c2a90e-fb18-461c-a411-d926c1af4481,2688c779-3e34-4848-9fce-d5de5ba24156,59d48ae8-e9aa-472d-b27a-a7f2eb143d99,f1ff51ac-2b1a-408c-91c3-c04d8feb23d6,4dde1573-5dd2-4d97-bd77-2c6e355ebd89,8bc64f1e-4422-4812-ac7a-9499b43c1bf2,195a0ca1-328e-40f9-bbee-6e6a05824b65,db9f2206-e10f-4495-87b7-827d9f4acd42,479127ec-4bfc-4f11-86ba-1a605e887eb5,b3c5636b-3c6e-418d-9275-4e7914518672,0058ad6c-29e2-436c-ac27-690ee474b06d,65d0bf61-0142-436b-838a-235a8b0f6dd3,6efd826f-c144-4fbf-bb81-df01d360c871,fc220fc4-012f-4703-9b9d-e7ea22c83dd3,c531fff6-784a-4c6f-8120-c22a3b402ffb,767b538a-f1fe-403d-988a-96d493c6e7ee,bf658ca4-44a5-4f32-8cb1-8bcb46022e91,22280da7-65b3-4598-8899-2df06f93c7b1,e5838cea-828f-4695-865b-a0b1843057df,14f83ce8-b0bd-483b-8f5f-f2fd4aa96357,a8821fe9-46f6-4a1c-96aa-7c45cdfefa70,edceee37-8bad-4607-8164-95f4a1a7e43c,904ddb3d-f3d1-4970-a8e6-a4d676a270af,698e79a8-3009-4a6c-a765-c999e8836e07,775c82d0-2ddb-4897-ae22-837da3f8a3a0,fc74b83a-94e6-4c9d-a2d3-6716f5002e44,15359a7a-910f-4b69-b2d9-73203ed25123,fe635719-66ba-440b-aab8-624c95b843e3,95f404c8-3f5f-4bf5-a5ba-c2f681b72afb,7e99b990-a72e-4705-ba9b-34b770b84a22,b91204b2-29f2-49bf-8078-6b8bf35bf190,ad777370-25a1-4ac9-a4a0-5281b214c5b4,5df503c1-aead-4031-9be7-21f2fd465621,6e986b8b-1f52-466a-8864-9e2b3d5fb035,324cfcf2-2fe8-4f40-91d1-04a0cf2df95b,039cfe9a-3a87-4a9f-8e61-4141e221dd3b,24471c29-ae86-431d-a665-0c0cfe178c5e,6904c4ee-a66d-4e48-a3c9-c75494388fc6,06dd81a5-a979-4dfd-b509-e9a9511bba32,04e28aef-d069-45d6-b21a-f89aa0d38c2a,433ac275-b06e-4414-b68c-ad678a79e7f4,1927430e-3eb2-4a2f-9514-b146792aac4f,59d0d273-3a0e-4970-b0f3-2fcd87e98ec4,13b35e7a-31d6-490d-8007-97d803430146,bda141b2-f8a2-419a-a2db-203472b40990,da6cf3db-50a5-4382-afed-40980e5355b1,8f5471db-3b98-4ba3-80c8-a643b26fc8ab,2764f0e3-623d-48ee-84b4-ba9735da77ec,39e98af1-62e5-455f-af8f-36a5fae29595,6e9403f1-7cd0-4f30-b547-290f0e847391,71724063-76da-4671-84b0-cc932916c1b9,6a5359ee-1b04-4645-b25d-a895599dd978,8adaf8a4-40d3-4eea-b428-6bf35178dc1d,5fc9fa20-3fc7-4913-a01e-c99f348f8ca2,8257ff95-c94b-4db6-afef-bb7d6c4e7a95,9a239dd6-99aa-4f74-b3f1-996f8687231d,f94dbc49-5f04-422d-8429-d3d73b4a01ef,9606d0c8-3191-4015-9591-8b0595d2b935,734fa4c8-db9e-474e-a623-80e97b9d7ce0,4c2ab1bc-6a5c-4119-a36f-63506fe28220,209a062b-7edd-489d-b534-4193ca3cf2d3,f2a7db54-77bb-4e45-adfe-2e1030f928b8,d33bb00d-e2ce-4ae3-a4fd-bc44ba3007c7,cc0c0805-4e9d-4578-a693-5ef70a255d0f,2944d38e-3a79-4220-8883-e1f9fae0893a,09c05dfb-8e43-4391-8701-4f12e3a64f7c,202d5a21-cd4d-4d45-a472-b2bdc4b007f9,85382c25-07d1-4bc6-ae0b-3fbe8cf61636,53c65434-70ca-4651-b2f5-2a2d4d11d293,26c397b1-d757-44a7-9d88-93702cf2d90d,a45a88ec-4bff-46a3-a16c-379ba4094c8e,882bc292-2d21-4191-8a8f-dcca989eebe5,4a43b312-fdb3-46e1-94bf-af70d1a1b393,fcfac8cb-043e-4512-933d-f426f2af9ff6,3d3f08ba-fb9f-4ede-828b-e96a8116f658,ad84d760-1759-4753-a082-a1fb8ab7c7a9,229cce59-5738-4250-ad2e-24b3c56758fa,687422f4-e8a2-407d-b001-d75bdbd394e2,87784f64-f560-45af-bd01-f39b976b980e,6861f1fa-a95b-46be-91bc-db08b26b10fb,611eeeb2-5f3f-4322-865e-3972cfa099f5,a49c487c-b88b-4a6e-af71-5fc01ec6d183,b8fb8e70-125b-4ea1-b53a-aee8a6c24ff8,de9a21c7-b94a-4c8b-9320-9221c1ac42a3,59843fd1-0107-4207-9fab-6b94eb234298,7265607c-5709-485f-b17c-57ceafa9376e,8ce801c6-3173-4938-87ed-9a5f016ed48e,8e9e3d03-d25a-4ba7-b54d-77bfb93bf1ca,305abf9c-1349-43cb-b37e-967332d1d0e0,94ec0148-4627-421d-9b15-4ad0152f53bb,4e94e37e-e019-43cb-aacc-e4b6c19f6415,295ccef0-7126-4228-b701-3b8f01068fc2,f3a54de2-e16e-4c14-a73b-8e5728d407ba,9643329c-c060-4549-9425-5cf2b7fb34ff,fa89ac2e-39d0-4417-a51d-5b1d91c77719,15786d47-caca-4726-a03e-05c170d5e4df,906fa0d9-2fe1-4a4d-93c9-390b1eec1f46,3b449b43-71d5-4ead-b6b4-bef73bd7d5be,45c4186a-73a1-419a-acd2-90fafef08eb9,3aef8a4f-ce36-476e-8c77-c056f9ff9c86,3557058e-8ae1-4109-8828-26eeceb1c827,8cba708a-3d19-4c68-b74c-8e546a6119fa,b75ef394-f3a3-4763-ba79-2a746dd0acb9,8d9dadd2-7efc-4c30-a066-57a8ca1364cf,7c03416a-c1fd-488d-86f1-29392384241a,35dd34eb-473a-45d9-8128-b7a1e8d82a66,ca2fc573-262c-4a4e-92d6-e3ed142d2490,303fe7e5-da13-4229-9d1a-a98ff7d198b8,0a0780af-2511-414b-aa7b-f048ec121982,830a31c8-42fb-43f7-99ff-239cc25df3ea,a387f59e-779b-4661-bb76-b10ccd40147f,02c09acc-56c2-4d13-a1b0-705ea6f7ddd6,29ad6ecc-6f3e-41af-9c0c-3294655640b3,d899b43e-aec5-4bb2-9c49-4db796c369e0,5ccd5216-d8c4-45be-a7bb-d7cd50b439e3,88762d64-a2f9-48a0-b5a7-6922859feefd,b28ea0bc-9601-4e7c-820b-0b8733f5a76a,5718e10f-719b-41fa-aeb3-72a6075e1e26,3dc68f6e-3c02-45e3-950b-13b0b85751e3,fa0f0000-f79e-4444-9064-341ea3b31ca7,ba8164c7-51d9-4de0-bdce-dfc271c462cc,342f1bb7-d5b1-41f0-a2a4-4cfc8e24cb19,d1e2ce19-52f4-43d3-9960-f45acb37e8a0,db771ab4-3182-4072-aa2f-804bfccbc8bd,587f5536-262e-4c80-a3e7-f10e37130ff3,a8ce05c6-8e78-40f2-b319-152cfecf9c23,4ed833d3-8f6e-4f1a-8628-154f00884b48,2df78434-4b2d-4f79-802e-725ff4e4da4a,c314e8fd-52e5-49e3-ab95-98a26ef87d01,e61285c3-fdf9-433f-80fd-3462f2106c23'
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