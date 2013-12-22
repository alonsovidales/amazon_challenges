package main
import "fmt"

/**
 * @author Alonso Vidales <alonso.vidales@tras2.es>
 * @date 2013-11-12
 */

// The length is the total minutes of the day plus one, the last one will be
// used as end point
var minutes [24 * 60 + 1]bool

/**
 * Retrns a list with all the available time slots composed by the start and end
 * times in minutes
 */
func get_slots(slot_time int) (free_slots [][2]int) {
    in_free_slot := false
    from_min := 0

    // Loop over all the minutes of the day and get the free slots with the
    // miniun lenght specified, easy :)
    for minute := 0; minute <= 24 * 60; minute++ {
        // This minute is free
        if !minutes[minute] {
            if !in_free_slot {
                in_free_slot = true
                from_min = minute
            }
        } else {
            if in_free_slot {
                in_free_slot = false
                if minute - from_min >= slot_time {
                    // Special case, this is the last of the minutes of the day
                    if minute == 24 * 60 {
                        free_slots = append(free_slots, [2]int{from_min, 0})
                    } else {
                        free_slots = append(free_slots, [2]int{from_min, minute})
                    }
                }
            }
        }
    }

    return free_slots
}

/**
 * Set as true all the minutes for this time slot, true indicates that this minute is not free
 */
func add_new_slot(slot_start_h int, slot_start_m int, slot_end_h int, slot_end_m int) {
    start_min := slot_start_h * 60 + slot_start_m
    end_min := slot_end_h * 60 + slot_end_m

    for pos := start_min; pos < end_min; pos++ {
        minutes[pos] = true
    }

    //fmt.Println(start_min, "-", end_min, ":", minutes)
}

func main() {
    var slots, slot_min int
    var slot_start_h, slot_start_m, slot_end_h, slot_end_m int

    for i:= 0; i < 24 * 60; i++ {
        minutes[i] = false
    }
    minutes[24 * 60] = true

    fmt.Scanf("%d %d", &slots, &slot_min)

    for slot := 0; slot < slots; slot++ {
        fmt.Scanf("%d %d %d %d", &slot_start_h, &slot_start_m, &slot_end_h, &slot_end_m)

        add_new_slot(slot_start_h, slot_start_m, slot_end_h, slot_end_m)
    }

    for _, slot := range get_slots(slot_min) {
        fmt.Printf("%02d %02d %02d %02d\n", slot[0] / 60, slot[0] % 60, slot[1] / 60, slot[1] % 60)
    }
}
