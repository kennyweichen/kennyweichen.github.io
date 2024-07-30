Difference in Differences
================

# Introduction

The first time I heard about Difference in Differences was in the PhD
level longitudinal analysis class at Harvard with Dr. Tom Chen.

We had a student who was previously trained as an economist who raised
his hand and brought this concept up. As a bright-eyed Master’s student
who got a B+ in Introduction to Economics, I did not know what this
concept was.

Today, I’m going to try to learn a bit more about it.

After a solid 20 minutes of browsing the web, it’s reductively just
introducing an interaction term between time and treatment…

Walking through this example:

``` r
library(foreign)
mydata <-  read.dta("http://dss.princeton.edu/training/Panel101.dta")

mydata$time = ifelse(mydata$year >= 1994, 1, 0)

mydata$treated = ifelse(mydata$country == "E" |
mydata$country == "F" |
mydata$country == "G", 1, 0)

mydata$did = mydata$time * mydata$treated
```

``` r
didreg = lm(y ~ treated + time + did, data = mydata)
summary(didreg)
```


    Call:
    lm(formula = y ~ treated + time + did, data = mydata)

    Residuals:
           Min         1Q     Median         3Q        Max 
    -9.768e+09 -1.623e+09  1.167e+08  1.393e+09  6.807e+09 

    Coefficients:
                  Estimate Std. Error t value Pr(>|t|)  
    (Intercept)  3.581e+08  7.382e+08   0.485   0.6292  
    treated      1.776e+09  1.128e+09   1.575   0.1200  
    time         2.289e+09  9.530e+08   2.402   0.0191 *
    did         -2.520e+09  1.456e+09  -1.731   0.0882 .
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Residual standard error: 2.953e+09 on 66 degrees of freedom
    Multiple R-squared:  0.08273,   Adjusted R-squared:  0.04104 
    F-statistic: 1.984 on 3 and 66 DF,  p-value: 0.1249

``` r
didreg1 = lm(y ~ treated*time, data = mydata)
summary(didreg1)
```


    Call:
    lm(formula = y ~ treated * time, data = mydata)

    Residuals:
           Min         1Q     Median         3Q        Max 
    -9.768e+09 -1.623e+09  1.167e+08  1.393e+09  6.807e+09 

    Coefficients:
                   Estimate Std. Error t value Pr(>|t|)  
    (Intercept)   3.581e+08  7.382e+08   0.485   0.6292  
    treated       1.776e+09  1.128e+09   1.575   0.1200  
    time          2.289e+09  9.530e+08   2.402   0.0191 *
    treated:time -2.520e+09  1.456e+09  -1.731   0.0882 .
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Residual standard error: 2.953e+09 on 66 degrees of freedom
    Multiple R-squared:  0.08273,   Adjusted R-squared:  0.04104 
    F-statistic: 1.984 on 3 and 66 DF,  p-value: 0.1249
