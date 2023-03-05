
fn main() {
    let mut total: u32 = 0;

    for i in 2..1_000_000_000 {
        let mut power_sum: u32 = 0;

        let mut j: u32 = i;

        while j != 0 {
            power_sum += (j % 10).pow(5);
            j /= 10;
        }

        if power_sum == i { total += i; }
    }

    println!("{}", total);
}
