import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print ('Ready')
    print (client.user.id)
    game = discord.Game('"-도움" 을 쳐주세요')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    message.content.startswith('렉스봇'):
    await message.channel.send('네')
if message.content.startswith('-영상날짜'):
    await  message.channel.send('1주일에 5번')
if message.content.startswith('-정보'):
    await message.channel.send(' 초와멤버 회장,  렉스봇 코드 개발자,와이렉스 커뮤니티 군대커뮤니티 마피아서버 총관리자')
    if message.content.startswith('-자기소개 '):
    await message.channel.send('안녕하세요 저는 렉스봇 입니다 저는 조금까칠한 성격이에요 좋아하는건 와이렉스tv 초와멤버 고기입니다 렉스봇에 추가문의가 있으시다면 개발자나 부개발자 에게 문의해주세요 개발자 보는법은 "렉스야 개발자"라고 명령어를 쳐주세요
    if message.content.startswith('헬레나'):
        await message.channel.send('바보')
    if message.content.startswith('크리스):
    await message.channel.send('천재')
    if message.content.startswith('흑돼지'):
        await message.channel.send('마시쩡')
    if message.content.startswith('-이야기'):
        await message.channel.send('-무서운이야기,-재밌는이야기')
    if message.content.startswith('-재밌는이야기'):
        await message.channel.send('아직 안만들었어요;;')
    if message.content.startswith('-무서운이야기'):
        await message.channel.send('와이렉스가 여친이 있어요 사실뻥이에요')
    if message.content.startswith('-스포일러'):
        await message.channel.send('선택해 주세요/-크게될놈/-어밴져스 앤드게임/주의! 간단하게 스포합니다')
    if message.content.startswith('-어밴져스 앤드게이'):
        await message.channel.send('캡틴레전드 토르뚱보 마지막에 캡틴어밴져스 은퇴 마지막 아이언맨 "나는아이언맨 이다" 그리고 아이언맨죽음')
    if message.content.startswith('-크게될놈'):
        await message.channel.send('사형처리 김기강')
    if message.content.startswith('렉스봇 속담'):
        await message.channel.send('한사진을 보고 1마리의 개가 짖는다 그개가 짖는걸보고 100마리의 개가 잊는다)
    if message.content.startswith('렉스봇 속담'):
        await message.channel.send('싫어')
    if message.content.startswith('-서버링크'):
        await message.channel.send('https://discord.gg/KgajrWz%27)
    if message.content.startswith('렉스봇 안녕'):
        await message.channel.send('안녕')
    if message.content.startswith('렉스봇 안녕'):
        await message.channel.send('안녕하세요 렉스봇입니다')
    if message.content.startswith('렉스봇 안녕'):
        await message.channel.send('렉스봇 처음보십니까?')
    if message.content.startswith('렉스봇 안녕'):
        await message.channel.send('초면에 반말이세요?')
    if message.content.startswith('핸섬마라오'):
        await message.channel.send('바....에헴....')
    if message.content.startswith('-렉스봇 추가문의'):
        await message.channel.send('와이렉스 님께 문의해주세요^^')
    if message.content.startswith('렉스봇 금사빠'):
        await message.channel.send('금요일에 피자먹고 사이다 빠샤')
    if message.content.startswith('-15금'):
        await message.channel.send('-시발-존나-ㅇㅅㅇ')
    if message.content.startswith('-시발'):
        await message.channel.send('먼저간다 라는뜻')
    if message.content.startswith('-존나'):
        await message.channel.send('남자의 중요한 부분을 비하하는말')
    if message.content.startswith('-ㅇㅅㅇ'):
        await message.channel.send('우스워 라는뜻이다')
    if message.content.startswith('-출처')
    await message.channel.send('샌즈#5635님이 만들어 주셨습니다. / 소스 제작자 : invalid-user 이분입니다.')
client.run('NTczMDMxMDY3Mzk3NjUyNDgw.XMk6_Q.izcFZWHfMw7hzNlOYzKLOstyKn0')


