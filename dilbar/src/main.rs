use std::ops::{Add, Deref};
use std::collections::vec_deque::VecDeque;

#[derive(Debug, Copy, Clone)]
struct Pos([i16; 2]);

const DIRECTIONS: [Pos; 4] = [
    Pos([ 1, 0]),
    Pos([ 0, 1]),
    Pos([-1, 0]),
    Pos([ 0,-1]),
];

impl Pos{
    fn to_idx(&self, board: &Board) -> usize{
        (self[0]*board.size[1]+self[1]) as usize
    }
    fn in_bounds(self, board: &Board) -> Option<Pos>{
        if (0..board.size[0]).contains(&self[0]) 
        && (0..board.size[1]).contains(&self[1]){
            Some(self)
        }else{
            None
        }
    }
}

impl Add for Pos{
    type Output = Self;
    fn add(self, other: Self) -> Self{
        [
            self[0]+other[0],
            self[1]+other[1],
        ].into()
    }
}
impl From<[i16; 2]> for Pos{
    fn from(thing: [i16; 2]) -> Self{
        Self(thing)
    }
}
impl Deref for Pos{
    type Target = [i16; 2];
    fn deref(&self) -> &Self::Target{
        &self.0
    }
}

#[derive(Debug, Copy, Clone)]
struct BoardCell{
    occupancy: u16,
    // -1 for occupied or unreachable
    closest_snake: i16,
    closest_distance: u16,
}

#[derive(Debug, Copy, Clone)]
struct Board{
    size: Pos,
}

fn calculate_ownership(board_cells: &mut Vec<BoardCell>, board: &Board, snakes: &Vec<(Pos, u8)>){
    let mut cycle = 0;
    let mut open_list = VecDeque::<(u16, Pos)>::new();
    for (snake_id, (snake_head, snake_length)) in snakes.iter().enumerate(){
        open_list.push_back((0, *snake_head));
        while let Some((dist, possib)) = open_list.pop_back(){
            let cell = &mut board_cells[possib.to_idx(&board)];
            cycle += 1;
            if (
                cell.closest_distance > dist
                || (cell.closest_distance == dist && cell.closest_snake!=(snake_id as i16) && snakes[cell.closest_snake as usize].1 /*<= if our snake is 0, otherwise use <*/ <= *snake_length)
            ) && cell.occupancy < dist+1{
                cell.closest_distance = dist;
                cell.closest_snake = snake_id as i16;
                for &dir in DIRECTIONS.iter(){
                    if let Some(landing) = (possib+dir).in_bounds(&board){
                        open_list.push_back((dist+1, landing));
                    }
                }
            }
        }
    }
    println!("Cycle Count: {}", cycle);
}

fn display_board(board: &Board, board_cells: &Vec<BoardCell>){
    for y in 0..board.size[1]{
        for x in 0..board.size[0]{
            let pos: Pos = [x, y].into();
            let snake = board_cells[pos.to_idx(board)].closest_snake;
            if snake == -1{
                print!("  ");
            }else{
                print!("{} ", snake);
            }
        }
        println!("");
    }
}

fn main() {
    let board = Board{size: [19, 19].into()};
    let mut board_cells = vec![
        BoardCell{
            occupancy: 0,
            closest_snake: -1,
            closest_distance: u16::max_value()
        };
        (board.size[0]*board.size[1]) as usize
    ];
    board_cells[1].occupancy = 100;
    board_cells[35].occupancy = 100;
    board_cells[15].occupancy = 100;
    board_cells[233].occupancy = 100;
    board_cells[261].occupancy = 100;
    board_cells[63].occupancy = 100;
    board_cells[82].occupancy = 100;
    board_cells[183].occupancy = 100;
    board_cells[13].occupancy = 100;
    board_cells[162].occupancy = 100;

    // u8 is snake's length
    let snakes: Vec<(Pos, u8)> = vec!(
        ([0, 0].into(), 3),
        ([0, 18].into(), 4),
        ([18, 0].into(), 3),
        ([18, 18].into(), 3)
    );

    calculate_ownership(&mut board_cells, &board, &snakes);

    display_board(&board, &board_cells);
}
