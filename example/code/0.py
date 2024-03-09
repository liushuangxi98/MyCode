import re

# 定义一个包含命名组的模式
pattern = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')

# 对字符串进行匹配
match = pattern.match('2024-01-30')

# 使用groupdict()方法获取所有命名组
result = match.groupdict()

print(result)  # 输出：{'year': '2024', 'month': '01', 'day': '30'}
