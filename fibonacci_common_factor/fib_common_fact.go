package main
import "fmt"

var fib_cache []int64

func smallest_common_fact(i int64, k int64) int64 {
    var min, num int64

    if (i < k) {
        min = i
    } else {
        min = k
    }

    for num = 2; num <= min; num++ {
        if (i % num == 0) && (k % num == 0) {
            return num
        }
    }

    return 1
}

func resolve(num int64) (value int64, common_fact int64) {
    for _, v := range fib_cache {
        common_fact = smallest_common_fact(v, num)
        if (common_fact != 1) {
            return v, common_fact
        }
    }

    prev := fib_cache[len(fib_cache) - 2]
    value = fib_cache[len(fib_cache) - 1]

    for (true) {
        prev_value := prev
        prev = value
        value += prev_value
        fib_cache = append(fib_cache, value)

        common_fact = smallest_common_fact(num, value)
        if (common_fact != 1) {
            return value, common_fact
        }
     }

     return value, common_fact
}

func main() {
        var problems int
        var number int64
        fib_cache = append(fib_cache, 1)
        fib_cache = append(fib_cache, 1)

        fmt.Scanf("%d", &problems)

        for i := 0; i < problems; i++ {
            fmt.Scanf("%d", &number)
            value, common_fact := resolve(number)

            fmt.Println(value, common_fact)
        }
}
