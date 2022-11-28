import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { useNavigate } from 'react-router-dom';

const RecipeCard = ({ data }) => {
    const navigate = useNavigate();
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
                {data?.name}
            </Typography>
            <Typography variant="body2" color="text.secondary">
                Category: {data?.category?.name} | Cuisine: {data?.area?.name}
            </Typography>
            </CardContent>

            <CardActions>
                <Button size="small" onClick={() => navigate(`/recipe/${data?.id}`)}>View</Button>
            </CardActions>
        </Card>
    );
}

export default RecipeCard;