import { useEffect, useState } from 'react';
import { Grid, Typography, Stack, useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';

function IdentificationCard() {
    const theme = useTheme();
    const isMobile = useMediaQuery(theme.breakpoints.down('md'));

    const [value, setValue] = useState({});

    useEffect(() => {
        const getRes = async () => {
            try {
                const url = 'https://dev2.mcaq.me/introducing';
                const res = await fetch(url, {
                    method: 'GET'
                });
                const data = await res.json();
                if (res.ok) {
                    console.log('data->', data);
                    setValue(data);
                } else {
                    console.log('error', data);
                }
            } catch (e) {
                console.log(e.message, true);
            }
        };
        getRes();
    }, []);
    return (
        <Stack mt={isMobile ? '50%' : '5%'} justifyContent="center" alignItems="center">
            <Grid
                container
                borderColor="red rgb(240,30,50,.7) green"
                justifyContent="center"
                alignItems="center"
                width={isMobile ? '100%' : '80vw'}
                height={isMobile ? '50%' : '80vh'}
                p={isMobile ? '2% 2%' : '4% 4%'}
                sx={{
                    backgroundImage: `linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),url(${value.background_image})`,
                    backgroundPosition: 'center',
                    backgroundRepeat: 'no-repeat',
                    backgroundSize: 'cover',
                    backgroundColor: 'linear - gradient(94.23deg,#5374fa 12.41 %, #fd9179 52.55 %, #ff6969 89.95 %)'
                }}
            >
                <Stack
                    backgroundColor="transparent"
                    justifyContent="center"
                    alignItems="center"
                    direction={isMobile ? 'column' : 'row'}
                    width={isMobile ? '100%' : '70vw'}
                    height={isMobile ? '40%' : '100%'}
                    p={isMobile ? '3% 0' : '0 0'}
                    border={isMobile ? '3px solid white' : '5px solid white'}
                >
                    <Grid item xl={5} align="center" lg={5} sm={12} xs={12} direction="column">
                        <Grid container align="center">
                            <Grid item xl={12} lg={12} sm={12} xs={12}>
                                <img src={value.profile_picture} alt="" width={isMobile ? '50%' : '50%'} style={{ borderRadius: '50%' }} />
                            </Grid>
                            <Grid item xl={12} lg={12} sm={12} xs={12}>
                                <Typography
                                    fontSize={isMobile ? '18px' : '36px'}
                                    color="#FFFFFF"
                                    fontWeight={isMobile ? '400px' : '700px'}
                                    p={isMobile ? '0% 0' : '0 0'}
                                >
                                    {value.title}
                                </Typography>
                            </Grid>
                        </Grid>
                    </Grid>
                    <Grid
                        item
                        xl={7}
                        lg={7}
                        sm={12}
                        xs={12}
                        textAlign={isMobile ? 'center' : ''}
                        p={isMobile ? '4% 3%' : '0 0'}
                        direction="column"
                    >
                        <Grid container>
                            <Grid item xl={12} lg={12} sm={12} xs={12}>
                                <Typography
                                    textAlign={isMobile ? 'center' : ''}
                                    fontSize={isMobile ? '18px' : '36px'}
                                    color="#FFFFFF"
                                    fontWeight={isMobile ? '400px' : '700px'}
                                >
                                    {value.name}
                                </Typography>
                            </Grid>
                            <Grid item xl={12} lg={12} sm={12} xs={12} p="4% 0" direction="row">
                                <Typography fontSize={isMobile ? '12px' : '20px'} color="#FFFFFF" fontWeight={isMobile ? '400px' : '700px'}>
                                    Age: {value.age} <span> Location: {value.location} </span>
                                </Typography>
                            </Grid>
                        </Grid>
                        <Grid container>
                            <Grid item xl={12} lg={12} pr="5%" sm={12} xs={12}>
                                <Typography fontSize={isMobile ? '12px' : '20px'} color="#FFFFFF" fontWeight={isMobile ? '400px' : '700px'}>
                                    {value.backstory}
                                </Typography>
                            </Grid>
                        </Grid>
                    </Grid>
                </Stack>
            </Grid>
        </Stack>
    );
}

export default IdentificationCard;
