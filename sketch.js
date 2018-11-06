const view_scale = 350;
const table_width = 1.2192 * view_scale;
const table_height = 2.1336 * view_scale;
const cushion_width = 0.07 * view_scale;
const frame_width = 0.03 * view_scale;
const garden_line = 0.4318 * view_scale;
const ball_diameter = 0.0508 * view_scale;
const pocket_diameter = 0.086 * view_scale;
const ball_offset = 0.866025;

let balls = []

const felt_colour = [27, 137, 38]
const frame_colour = [96, 62, 19]

let white_ball;
let black_ball;

function setup() {
    createCanvas(1000, 1000);
    white_ball = new Ball(table_width/2, garden_line, [255, 255, 255])
    black_ball = new Ball(table_width/2, table_height - garden_line, [50, 50, 50])

    balls.push(white_ball);
    balls.push(black_ball);

    for(let i=0;i<5;i++){
        for(let j=i;j>=0;j--){
            let x = (table_width/2) - (i * ball_diameter/2) + (j * ball_diameter);
            let y = table_height - garden_line + 2 * ball_diameter - j * ball_diameter * ball_offset;
            balls.push(new Ball(x, y, [i*20, 0, 0]));
        }
    }
}

function draw() {
    background(0);
    translate(width/2 -table_width/2, height/2-table_height/2)
    fill(frame_colour);
    rect(-cushion_width-frame_width, -cushion_width-frame_width, table_width+2*cushion_width+2*frame_width, table_height+2*cushion_width+2*frame_width);
    fill(felt_colour);
    rect(-cushion_width, -cushion_width, table_width+2*cushion_width, table_height+2*cushion_width);
    fill(felt_colour);
    rect(0, 0, table_width, table_height);

    line(0, garden_line, table_width, garden_line)
    ellipse(table_width / 2, table_height - garden_line, 2, 2);

    fill(0)
    ellipse(0, 0, pocket_diameter, pocket_diameter);
    ellipse(table_width, 0, pocket_diameter, pocket_diameter);
    ellipse(0, table_height/2, pocket_diameter, pocket_diameter);
    ellipse(table_width, table_height/2, pocket_diameter, pocket_diameter);
    ellipse(table_width, table_height, pocket_diameter, pocket_diameter);
    ellipse(0, table_height, pocket_diameter, pocket_diameter);
    
    
    for(let i=0;i<balls.length;i++) {
        let ball = balls[i];
        ball.update();
        ball.draw();
    }
}

function Ball(x, y, colour) {
    this.pos = createVector(x, y)
    this.colour = colour;

    this.update = function() {

    }
    this.draw = function() {
        fill(this.colour)
        ellipse(this.pos.x, this.pos.y, ball_diameter, ball_diameter);
    }
}