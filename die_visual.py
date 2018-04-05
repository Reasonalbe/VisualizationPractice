from die import Die
import pygal

die = Die()
#投掷骰子，并将结果存于一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#每一面出现的频率
frequency = []
for roll_num in range(1, die.num_sides+1):
    frequency.append(results.count(roll_num))

#结果可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels=[str(i) for i in range(1, die.num_sides+1)]
hist._x_title = "Results"
hist._y_title = "Frequency of Results"

hist.add("D6", frequency)
hist.render_to_file('die_visual.svg')

