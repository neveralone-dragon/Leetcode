595.大的国家
# Write your MySQL query statement below
SELECT name,population,area
from World
WHERE area >= 3000000 ||
population >= 25000000;
这里看到有个评论提到了or和union的区别，我去stackoverflow上面查了一下，具体链接放在末尾。
大致意思是: 对于单列来说，用or是没有任何问题的，但是or涉及到多个列的时候，每次select只能选取一个index，
如果选择了area，population就需要进行table-scan，即全部扫描一遍，但是使用union就可以解决这个问题，分别使用area和population上面的index进行查询。
但是这里还会有一个问题就是，UNION会对结果进行排序去重，
可能会降低一些performance(这有可能是方法一比方法二快的原因），所以最佳的选择应该是两种方法都进行尝试比较。 （stackoverflow链接:

# Write your MySQL query statement below
SELECT product_id
FROM Products
WHERE low_fats = 'Y' and
recyclable = 'Y';


# 584
# Write your MySQL query statement below
SELECT name
FROM customer
WHERE referee_id <> 2 OR referee_id is NULL;

# Write your MySQL query statement below
SELECT customers.name as 'Customers'
from customers
where customers.id not in(
    SELECT customerid from orders
);
