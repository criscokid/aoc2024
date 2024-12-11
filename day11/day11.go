package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type iterationJob struct {
	value      int64
	iterations int
}

func main() {
	b, err := os.ReadFile("input1.txt")
	if err != nil {
		panic(err)
	}
	values := []int64{}
	for _, s := range strings.Fields(string(b)) {
		v, err := strconv.ParseInt(s, 10, 64)
		if err != nil {
			panic(err)
		}
		values = append(values, v)
	}
	const numJobs = 8
	jobs := make(chan iterationJob, numJobs)
	results := make(chan int64, numJobs)

	for w := 0; w < numJobs; w++ {
		go worker(jobs, results)
	}

	total := int64(0)
	for _, v := range values {
		jobs <- iterationJob{value: v, iterations: 75}
	}
	close(jobs)

	for a := 0; a < numJobs; a++ {
		total += <-results
	}

	fmt.Println(total)
}

func worker(jobs <-chan iterationJob, results chan<- int64) {
	for j := range jobs {
		results <- process(j.value, j.iterations)
	}
}

func process(value int64, iteration int) int64 {
	if iteration == 0 {
		return 1
	}

	if value == 0 {
		return process(1, iteration-1)
	}

	if int(math.Log10(float64(value))+1)%2 == 0 {
		str_value := fmt.Sprintf("%d", value)
		midPoint := len(str_value) / 2
		left, err := strconv.ParseInt(str_value[0:midPoint], 10, 64)
		if err != nil {
			panic(err)
		}
		right, err := strconv.ParseInt(str_value[midPoint:], 10, 64)
		if err != nil {
			panic(err)
		}
		t := int64(0)
		t += process(left, iteration-1)
		t += process(right, iteration-1)
		return t
	}

	return process(value*2024, iteration-1)
}
