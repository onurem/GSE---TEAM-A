import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Box from '@mui/material/Box';
import Alert from '@mui/material/Alert';
import TextsmsOutlinedIcon from '@mui/icons-material/TextsmsOutlined';
import TextareaAutosize from '@mui/material/TextareaAutosize';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Chip, Stack } from '@mui/material';
import ThumbDownOffAltIcon from '@mui/icons-material/ThumbDownOffAlt';
import LocalFireDepartmentIcon from '@mui/icons-material/LocalFireDepartment';
import ThumbUpIcon from '@mui/icons-material/ThumbUp';

const SAMPLE_SENTENCES = [
    "As long as the Lakers trash from now on, I could careless. And that's real.",
    "I wanna have sex with my mom fuck her right in that pussy where I came from",
    "You a woulda coulda shoulda ass hoe",
    "Glad I'm getting outta Atlanta. Nothing but a bunch of niggas in &amp; outta jail &amp; dumb bitches with mad kids fuckin em",
    "Who wants to get there nose in these bad bois then #scally #chav #sockfetish #stinking http://t.co/FeQxgN0W6I",
    "I got hicks lol",
    "This new twitter is confusing the shit out of me. Go back to south america bitch",
    "@_WhitePonyJr_ Ariza is a snake and a coward but at least he isn't a cripple like your hero Roach lmaoo",
    "@Poffalicious: Andrewbryant: Poff has double vision after 2 beers... Double pussy",
    "I teach u how to get curved? That's all I know",
    "Would you still love me when I'm no longer young and beautiful? No. Ugly monkey ass",
    "@Theo17100: http://t.co/BYj1HOyhmG this scally lad would get it",
    "A smuggler explains how he helped fighters along the Jihadi Highway",
    "@ItsNotAdam is bored supposed to be cute, you faggot?",
    "@jayswaggkillah: Jackies a retard #blondeproblems At least I can make a grilled cheese!"
]

export default function DemoForm() {
    const [CheckResult, setCheckResult] = React.useState(null)
    const [testId, setTestId] = React.useState(0)
    const [textVal, setTextVal] = React.useState('')
    const inputEl = React.useRef(null);

    const handleSubmit = (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);

        let opts = {
            'method': 'POST',
            'body': data
        }
        fetch(`https://hateless.herokuapp.com/v1/predict`, opts)
            .then(rs => rs.json())
            .then(rs => {
                setCheckResult(rs['confidences'])
            })
        // eslint-disable-next-line no-console
    };

    const handleChange = (e) => {
        setTextVal(e.target.value)
    }

    return (
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
                        value={textVal}
                        onChange={handleChange}
                        name="message"
                        minRows={4}
                        aria-label="maximum height"
                        placeholder="Sample text to analyze"
                        style={{ width: 400 }}
                    />
                    <Stack direction="row" spacing={1}>
                        <Button
                            type="submit"
                            fullWidth
                            variant="contained"
                        >
                            Check it
                        </Button>
                        <Button
                            fullWidth
                            variant="contained"
                            onClick={() => {
                                let newId = Math.floor(Math.random() * SAMPLE_SENTENCES.length);
                                setTextVal(SAMPLE_SENTENCES[newId])
                            }}
                        >
                            New random
                        </Button>
                    </Stack>
                    {CheckResult ?
                        <Box
                            sx={{
                                marginTop: 3,
                                display: 'flex',
                                flexDirection: 'column',
                                alignItems: 'center',
                            }}
                        >
                            <Stack direction="row" spacing={1}>
                                <Chip
                                    color="error"
                                    icon={<ThumbDownOffAltIcon />}
                                    label={'offensive: ' + Number(CheckResult['offensive_language'] * 100).toFixed(2) + "%"} />
                                <Chip
                                    color="secondary"
                                    icon={<LocalFireDepartmentIcon />}
                                    label={'hate_speech: ' + Number(CheckResult['hate_speech'] * 100).toFixed(2) + "%"} />
                                <Chip
                                    color="success"
                                    icon={<ThumbUpIcon />}
                                    label={'normal: ' + Number(CheckResult['neither'] * 100).toFixed(2) + "%"} />
                            </Stack>,
                            <Stack direction="row" spacing={1}>
                                <Chip
                                    icon={<LocalFireDepartmentIcon />}
                                    label={'sacarsm: ' + Number(0).toFixed(2)} />
                                <Chip
                                    icon={<ThumbUpIcon />}
                                    label={'sexism: ' + Number(0).toFixed(2)} />
                            </Stack>
                        </Box>
                        // <Alert onClose={() => { }}>
                        //     Offensive: {Number(CheckResult['offensive_language'] * 100).toFixed(2)}%,&nbsp;
                        //     Hate: {Number(CheckResult['hate_speech'] * 100).toFixed(2)}%,&nbsp;
                        //     Normal: {Number(CheckResult['neither'] * 100).toFixed(2)}%,&nbsp;
                        //     Sarcasm: {Number(0).toFixed(2)}%,&nbsp;
                        //     Sexism: {Number(0).toFixed(2)}%
                        // </Alert> :
                        : ''}
                </Box>
            </Box>
        </Container>
    );
}