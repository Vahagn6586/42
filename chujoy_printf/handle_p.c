/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_ptr.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 15:34:24 by vrafyan           #+#    #+#             */
/*   Updated: 2026/03/06 15:34:27 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	handle_p(va_list *arg)
{
	unsigned long	addr;
	char			*res;
	int				retval;

	addr = (va_arg(*arg, unsigned long));
	if (addr == 0)
	{
		ft_putstr("(nil)");
		return (5);
	}
	res = ft_itoa_base_low(addr, 16);
	ft_putstr("0x");
	ft_putstr(res);
	retval = ft_strlen(res);
	free(res);
	return (retval + 2);
}
