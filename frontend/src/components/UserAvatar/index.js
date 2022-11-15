import React from 'react';
import Avatar from '@mui/material/Avatar';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import PersonIcon from '@mui/icons-material/Person';
import { AppContext } from '../../constants';
import styles from "./styles.css"

const UserAvatar = () => {
    const { user } = React.useContext(AppContext)
    return (
        <Paper className="badge">
            <Avatar className="avatar" src={user?.picture}>
                <PersonIcon />
            </Avatar>
            <Typography className="username" variant="body1">
                {user?.name}
            </Typography>
            <Typography className="signout" variant="body2">
                Sign Out
            </Typography>
        </Paper>
    )
}

export default UserAvatar;