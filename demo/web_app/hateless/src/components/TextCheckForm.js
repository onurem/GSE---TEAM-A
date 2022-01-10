import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Alert from '@mui/material/Alert';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import TextsmsOutlinedIcon from '@mui/icons-material/TextsmsOutlined';
import TextareaAutosize from '@mui/material/TextareaAutosize';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';

function Copyright(props) {
    return (
        <Typography variant="body2" color="text.secondary" align="center" {...props}>
            {'Copyright © '}
            <Link color="inherit" href="https://mui.com/">
                Your Website
            </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}

const theme = createTheme();

export default function TextCheckForm() {
    const [CheckResult, setCheckResult] = React.useState(null)

    const handleSubmit = (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);

        let opts = {
            'method': 'POST',
            'body': data
        }
        fetch(`https://hateless.herokuapp.com/v0/predict`, opts)
            .then(rs => rs.json())
            .then(rs => {
                setCheckResult(rs)
            })
        // eslint-disable-next-line no-console
    };

    return (
        <ThemeProvider theme={theme}>
            <Container component="main" maxWidth="xs">
                <CssBaseline />
                <Box
                    sx={{
                        marginTop: 8,
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center',
                    }}
                >
                    <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                        <TextsmsOutlinedIcon />
                    </Avatar>
                    <Typography component="h1" variant="h5">
                        Hateless
                    </Typography>
                    <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
                        <TextareaAutosize
                            name="message"
                            maxRows={4}
                            aria-label="maximum height"
                            placeholder="Maximum 4 rows"
                            defaultValue="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
                            style={{ width: 400 }}
                        />
                        <Button
                            type="submit"
                            fullWidth
                            variant="contained"
                            sx={{ mt: 3, mb: 2 }}
                        >
                            Check it
                        </Button>
                        {CheckResult ?
                            <Alert onClose={() => { }}>
                                Offen: {Number(CheckResult[0]*100).toFixed(2)}%,&nbsp;
                                Hate: {Number(CheckResult[1]*100).toFixed(2)}%,&nbsp;
                                Other: {Number(CheckResult[2]*100).toFixed(2)}%
                            </Alert> : ''}
                    </Box>
                </Box>
                <Copyright sx={{ mt: 8, mb: 4 }} />
            </Container>
        </ThemeProvider>
    );
}