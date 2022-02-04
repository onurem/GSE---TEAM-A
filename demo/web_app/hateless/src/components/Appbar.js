import React from 'react'
import Typography from '@mui/material/Typography';
import MenuIcon from '@mui/icons-material/Menu';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import MuiAppBar from '@mui/material/AppBar';
import { styled } from '@mui/material/styles';
import { Avatar, Box, Button, Menu, MenuItem, Tooltip } from '@mui/material';
import { useAuth } from './AuthProvider';
import PopupState, { bindTrigger, bindMenu } from 'material-ui-popup-state';
import { useLocation, useNavigate } from 'react-router-dom';

const settings = ['Profile', 'Account', 'Dashboard', 'Logout'];
const getName = (path) => {
    console.log(path)
    switch (path) {
        case '/demo':
            return 'Demo';
        default:
            return 'Dashboard';
    }
}

export default function MyAppBar(props) {
    let auth = useAuth();
    let navigate = useNavigate();
    let location = useLocation();
    let path = location.pathname || "/";

    let open = props.open
    let drawerWidth = props.drawerWidth
    let toggleDrawer = props.toggleDrawer

    const AppBar = styled(MuiAppBar, {
        shouldForwardProp: (prop) => prop !== 'open',
    })(({ theme, open }) => ({
        zIndex: theme.zIndex.drawer + 1,
        transition: theme.transitions.create(['width', 'margin'], {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
        }),
        ...(open && {
            marginLeft: drawerWidth,
            width: `calc(100% - ${drawerWidth}px)`,
            transition: theme.transitions.create(['width', 'margin'], {
                easing: theme.transitions.easing.sharp,
                duration: theme.transitions.duration.enteringScreen,
            }),
        }),
    }));


    return (
        <AppBar position="absolute" open={open}>
            <Toolbar
                sx={{
                    pr: '24px', // keep right padding when drawer closed
                }}>

                <IconButton
                    edge="start"
                    color="inherit"
                    aria-label="open drawer"
                    onClick={toggleDrawer}
                    sx={{
                        marginRight: '36px',
                        ...(open && { display: 'none' }),
                    }}
                >
                    <MenuIcon />
                </IconButton>
                <Typography
                    component="h1"
                    variant="h6"
                    color="inherit"
                    noWrap
                    sx={{ flexGrow: 1 }}
                >
                    {getName(path)}
                </Typography>
                <Box sx={{ flexGrow: 0 }}>
                    <PopupState variant="popover" popupId="demo-popup-menu">
                        {(popupState) => (
                            <React.Fragment>
                                <Button
                                    variant="fab"
                                    {...bindTrigger(popupState)}>
                                    Setting
                                </Button>
                                <Menu {...bindMenu(popupState)}>
                                    <MenuItem onClick={popupState.close}>Profile</MenuItem>
                                    <MenuItem onClick={() => {
                                        auth.signout(() => navigate("/"))
                                        popupState.close()
                                    }}>Logout</MenuItem>
                                </Menu>
                            </React.Fragment>
                        )}
                    </PopupState>
                </Box>
            </Toolbar>
        </AppBar>
    )
}