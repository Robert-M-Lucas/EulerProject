use std::{fs, time::Instant};


fn main() {
    let contents = fs::read_to_string("input.txt").expect("File read failure");

    let mut data: Vec<Vec<u16>> = vec![vec![]];

    {
        let mut buffer = String::new();
        for c in contents.chars() {
            if c == ' ' {
                if buffer.is_empty() { continue; }
                let len = data.len();
                data[len - 1].push(buffer.parse().unwrap());
                buffer.clear();
            }
            else if c == '\n' || c == '\r' {
                if buffer.is_empty() { continue; }
                let len = data.len();
                data[len - 1].push(buffer.parse().unwrap());
                data.push(vec![]);
                buffer.clear();
            }
            else {
                buffer.push(c);
            }
        }
        if !buffer.is_empty() {
            let len = data.len();
            data[len - 1].push(buffer.parse().unwrap());
        }
    }

    let mut largest_found: u32 = 0;
    let mut remaining = Vec::new();

    remaining.reserve(data[0].len());
    for i in 0..data.len() {
        remaining.push(i);
    }

    let start = Instant::now();

    find_sum(0, &remaining, &mut largest_found, 0, &data, data.len());

    let end = start.elapsed();

    println!("{}", largest_found);
    println!("{:?}", end);
}

fn find_sum(column: usize, rows_remaining: &Vec<usize>, largest_found: &mut u32, current_sum: u32, data: &Vec<Vec<u16>>, max: usize) {
    if column == max {
        if current_sum > *largest_found { *largest_found = current_sum; }
        return;
    }

    if current_sum + (max - column) as u32 * 1000 < *largest_found {
        return;
    }

    for i in 0..rows_remaining.len() {
        let mut new_remaining = rows_remaining.clone();
        new_remaining.remove(i);
        let new_sum = current_sum + data[column][rows_remaining[i]] as u32;
        find_sum(column + 1, &new_remaining, largest_found, new_sum, data, max);
    }
}