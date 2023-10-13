from datascience import *
import numpy as np
import matplotlib.pyplot as plots
import matplotlib
matplotlib.use('TkAgg')
plots.style.use('fivethirtyeight')

top1 = Table.read_table('Data/top_movies.csv')
top2 = top1.with_column('Row Index', np.arange(top1.num_rows))
top = top2.move_to_start('Row Index')
top.set_format(make_array(3, 4), NumberFormatter)

print(top.take(make_array(3, 18, 100)), "\n")

print(top.where('Title', are.containing('Harry Potter')), "\n")

start = np.random.choice(np.arange(10))
print(top.take(np.arange(start, top.num_rows, 10)), "\n")

die = Table().with_column('Face', np.arange(1, 7, 1))
print(die, "\n")

die_bins = np.arange(0.5, 6.6, 1)
die.hist(bins = die_bins)
plots.title("Probability of dice rolls")
plots.show()

print(die.sample(10), "\n")

def empirical_hist_die(n):
    die.sample(n).hist(bins = die_bins)

empirical_hist_die(10)
plots.title("Roll the dice 10 times")
plots.show()

empirical_hist_die(100000)
plots.title("Roll the dice 100000 times")
plots.show()