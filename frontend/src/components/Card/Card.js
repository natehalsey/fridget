import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

export default function MediaCard({ data }) {
    //console.log(data);
    return (
    <Card sx={{ maxWidth: 345 }}>
        <CardMedia
        component="img"
        height="140"
        image={data?.image_url}
        alt="recipe img"
        />
        <CardContent>
        <Typography gutterBottom variant="h5" component="div">
            Name: {data?.name}
        </Typography>
        <Typography variant="body2" color="text.secondary">
            Category: {data?.category?.name} | Area: {data?.area?.name}
        </Typography>
        {/* <Typography variant="body2" color="text.secondary">
            Main Ingredients: {data?.ingredients_measurements[0]?.ingredient}
        </Typography> */}
        </CardContent>
        <CardActions>
        <Button size="small">Save</Button>
        <Button size="small">View</Button>
        </CardActions>
    </Card>
    );
}