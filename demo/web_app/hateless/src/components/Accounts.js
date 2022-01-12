import * as React from 'react';
import Link from '@mui/material/Link';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Title from './Title';
import Chip from '@mui/material/Chip';

// Generate Order Data
function createData(id, date, name, shipTo, amount) {
  return { id, date, name, shipTo, amount };
}

const rows = [
  createData(
    0,
    '16 Mar, 2019',
    'Elvis Presley',
    'User',
    'Create'
  ),
  createData(
    1,
    '16 Mar, 2019',
    'Paul McCartney',
    'User',
    'Review'
  ),
  createData(2,
    '16 Mar, 2019',
    'Tom Scholz',
    'User',
    'Create'
  ),
  createData(
    3,
    '16 Mar, 2019',
    'Michael Jackson',
    'User',
    'Create'
  ),
  createData(
    4,
    '15 Mar, 2019',
    'Bruce Springsteen',
    'User',
    'Create'
  ),
];

function preventDefault(event) {
  event.preventDefault();
}

export default function Accounts() {
  return (
    <React.Fragment>
      <Title>Recent activities</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell>Name</TableCell>
            <TableCell>Role</TableCell>
            <TableCell align="right">Action</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.date}</TableCell>
              <TableCell>{row.name}</TableCell>
              <TableCell>{row.shipTo}</TableCell>
              <TableCell align='right'><Chip label={row.amount} /></TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <Link color="primary" href="#" onClick={preventDefault} sx={{ mt: 3 }}>
        See more accounts
      </Link>
    </React.Fragment>
  );
}