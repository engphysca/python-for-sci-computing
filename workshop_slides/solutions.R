library(tidyverse)

# Plot highway miles per gallon hwy as
# the x-variable and city miles per gallon cty as the y-variable.

ggplot(data = mpg, mapping = aes(x = hwy, y = cty))

# Colour this plot by the vehicle's type of transmission trans.
ggplot(data = mpg,
       mapping = aes(x = hwy, y = cty, colour=trans)) +
  geom_point()

# (bonus): include a regression line on your plot!
ggplot(data = mpg,
       mapping = aes(x = hwy, y = cty)) +
  geom_point() +
  geom_smooth(method='lm')

ggplot(mpg, aes(hwy, cty)) +
  geom_point() +
  geom_smooth()


# set your working directory
setwd('Downloads/')

# read.csv() OR read_csv()
dino_data <- read_csv('data_dino.csv')
dino_data

# now let's plot the dino!
ggplot(data = dino_data,
       mapping = aes(x = horizontal, y = vertical)) +
  geom_point()

# load gapminder
library(gapminder)
# install gapminder
# install.packages('gapminder')

gapminder
?gapminder
str(gapminder)

# filter()
filter(gapminder, year > 1980)
gapminder %>% filter(year > 1980, country == "Canada", pop > 500)

# select()
colnames(gapminder)
gapminder %>% select(continent, year, lifeExp)

# chaioning commands together
gapminder %>%
  filter(year > 1980, country == 'United States', pop > 100000) %>%
  select(country, year, pop)

# Select the country, year, and lifeExp columns in the gapminder dataset,
# and look at life expectancy in Rwanda in 1987 and 1992.
gapminder %>%
  select(country, year, lifeExp) %>%
  filter(country=='Rwanda', year == 1987 & year == 1992)
