package main

import "fmt"
import "bufio"
import "os"
import "strconv"
import "strings"
import "regexp"
import "hash/crc32"

/**
 * @author Alonso Vidales <alonso.vidales@tras2.es>
 * @date 2013-11-12
 *
 * @description: This solution is based in convert the words in int values using
 *	crc32 and try to find the smallest subset that sum the same than the given
 *	words, doing this, we have a hight probability of find the correct sub set
 */

/**
 * Returns two arrays that includes only the words of the text ho matches with
 * the given words, one of the arrays is a list of the crc32 values of the words
 * and the other one the positions in the original string of this words
 */
func get_words_crc_pos(text []string, available_words map[uint64]bool) (text_word_pos []int, text_word_crc []uint64) {
    // Divide the original text in words, and assign a value to each word to be find
    for pos, word := range text {
	crc32 := uint64(crc32.Checksum([]byte(strings.ToLower(word)), crc32.IEEETable))
	_, found := available_words[crc32]
	if found {
	    text_word_crc = append(text_word_crc, crc32)
	    text_word_pos = append(text_word_pos, pos)
	}
    }

    return text_word_pos, text_word_crc
}

func Sum(a *[]uint64) (sum uint64) {
    for _, v := range *a {
	sum += v
    }
    return
}

func main() {
    bio := bufio.NewReader(os.Stdin)

    text, _ := bio.ReadString('\n')
    text = text[:len(text) - 1]
    words, _ := bio.ReadString('\n')
    words_int, _ := strconv.ParseInt(words[:len(words) - 1], 10, 0)

    var words_total_weight uint64
    words_total_weight = 0

    // Build a set with the given words in order to know if a word is included
    // or not with O(1)
    available_words := make(map[uint64]bool)
    for i:= 0; i < int(words_int); i++ {
	word, _ := bio.ReadString('\n')
	if word[len(word) - 1] == '\n' {
	    word = strings.ToLower(word[:len(word) - 1])
	}
	crc32 := uint64(crc32.Checksum([]byte(word), crc32.IEEETable))
	available_words[crc32] = true
	words_total_weight += crc32
	//fmt.Println("Words weight:", words_total_weight)
    }

    // Filter the string to get only the [a-z][A-Z] chars
    re, _ := regexp.Compile(`[^A-Za-z ]+`)
    text = string(re.ReplaceAll([]byte(text), []byte("")))
    //fmt.Println("After:", text)

    // Divide the original string in words and calculate the CRC for each one
    text_split := strings.Split(text, " ")
    text_word_pos, text_word_crc := get_words_crc_pos(text_split, available_words)

    //fmt.Println("Words Pos:", text_word_pos)
    //fmt.Println("Words CRC:", text_word_crc)
    smallest_str := text_split
    found := false

    // Get all the possible sub sets in order to find one of the that sums the
    // same than all the given words
    main_loog: for subset_lenght := len(available_words); subset_lenght <= len(text_word_crc); subset_lenght++ {
	//fmt.Println("Len:", subset_lenght)

	for pos := 0; pos <= len(text_word_crc) - subset_lenght; pos++ {
		text_len := text_word_pos[pos + subset_lenght - 1] + 1 - text_word_pos[pos]

	    if text_len < len(smallest_str) {
		subset := text_word_crc[pos:pos + subset_lenght]
		//fmt.Println("SubSetPos:", text_word_pos[pos:pos + subset_lenght])

		if Sum(&subset) == words_total_weight {
		    found = true
		    smallest_str = text_split[text_word_pos[pos] : text_word_pos[pos + subset_lenght - 1] + 1]
		    //fmt.Println("NewSmalles:", text_len, smallest_str)

		    // We have a winner :), a smallest string can't be found
		    if len(smallest_str) == len(available_words) {
			break main_loog
		    }
		}
	    }
	}
    }

    if !found {
        fmt.Println("NO SUBSEGMENT FOUND")
    } else {
        fmt.Println(strings.Join(smallest_str, " "))
    }
}
